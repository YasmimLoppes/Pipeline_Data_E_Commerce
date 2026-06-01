import pandas as pd
import numpy as np
from datetime import datetime
import os
from config import PATHS, BUSINESS_RULES
from scripts.utils import configurar_log, buscar_arquivo_mais_recente

logger = configurar_log("transformacao")

def transformar_dados(df_bruto):
    try:
        logger.info("Iniciando Processo de Transformação e Qualidade (Camada Silver)")

        # 1. Eliminação de linhas nulas nos campos vitais do negócio
        df = df_bruto.dropna(subset=BUSINESS_RULES["campos_obrigatorios"]).copy()
        
        # 2. Remoção de Duplicidades na chave primária do produto
        df = df.drop_duplicates(subset=['id'])

        # 3. Limpeza de limites lógicos de preços (Filtro Sanitário)
        preco_valido = (df['price'] >= BUSINESS_RULES["min_price"]) & (df['price'] <= BUSINESS_RULES["max_price"])
        df = df[preco_valido].copy()

        # 4. Aplicação das Regras e Fórmulas de Negócio (Estoque e Margens)
        df['preco_custo'] = round(df['price'] * (1 - BUSINESS_RULES["margem_lucro"]), 2)
        df['quantidade_estoque'] = BUSINESS_RULES["estoque_padrao"]
        df['valor_total_estoque'] = round(df['quantidade_estoque'] * df['preco_custo'], 2)
        df['margem_lucro_estimada'] = round(df['price'] - df['preco_custo'], 2)
        
        # 5. Padronização Textual (Garante consistência analítica)
        df['categoria_padrao'] = df['category'].str.strip().str.upper()
        df['nome_produto_padrao'] = df['title'].str.strip()

        # Extração das notas das avaliações imbricadas (Dicionário da API original)
        if 'rating' in df.columns:
            # Garante que dados em formato string de dicionário virem estruturas lógicas
            ratings_limpos = df['rating'].apply(lambda x: eval(x) if isinstance(x, str) else x)
            df['avaliacao_cliente'] = ratings_limpos.apply(lambda x: x.get('rate', 0.0) if isinstance(x, dict) else 0.0)
        else:
            df['avaliacao_cliente'] = 0.0

        # 6. Criação de Metadados de Auditoria da Carga
        df['data_processamento'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['origem_dado'] = "API_FAKE_STORE"

        # Seleção e Limpeza Final do Esquema da Tabela Silver
        colunas_finais = [
            'id', 'nome_produto_padrao', 'categoria_padrao', 'preco_custo', 
            'valor_total_estoque', 'margem_lucro_estimada', 'price', 
            'avaliacao_cliente', 'data_processamento', 'origem_dado'
        ]
        df_silver = df[colunas_finais].rename(columns={'id': 'id_produto', 'price': 'preco_venda_sugerido'})

        # Salvamento Físico da Camada Silver
        data_hoje = datetime.now().strftime("%Y%m%d")
        caminho_salvamento = os.path.join(PATHS["processed_data"], f"vendas_tratado_{data_hoje}.csv")
        df_silver.to_csv(caminho_salvamento, index=False, encoding='utf-8-sig')

        logger.info(f"Transformação concluída | Dados limpos salvos em: {caminho_salvamento}")
        print(f"✅ QUALIDADE E TRANSFORMAÇÃO OK! Arquivo gerado em: {caminho_salvamento}")
        
        return df_silver

    except Exception as erro:
        logger.error(f"Erro no motor de regras de negócio: {erro}", exc_info=True)
        print("❌ FALHA NA TRANSFORMAÇÃO. Verifique o arquivo logs/transformacao.log")
        raise

if __name__ == "__main__":
    try:
        arquivo_raw = buscar_arquivo_mais_recente(PATHS["raw_data"], "vendas_bruto_*.csv")
        df_original = pd.read_csv(arquivo_raw)
        transformar_dados(df_original)
    except Exception as e:
        print(f"Erro ao executar transformação isolada: {e}")