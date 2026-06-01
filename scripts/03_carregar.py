import pandas as pd
import boto3
from sqlalchemy import create_engine, text
from datetime import datetime
import os
import logging
from config import PATHS, AWS_CONFIG
from scripts.utils import configurar_log, buscar_arquivo_mais_recente

logger = configurar_log("carga")

def carregar_dados(df, caminho_local_original):
    print("🗄️ Inicializando Carga e Distribuição de Dados...")
    try:
        # ==================================================
        # PASSO 1: GRAVAÇÃO NO BANCO RELACIONAL SQL (SQLite)
        # ==================================================
        engine = create_engine('sqlite:///banco_vendas_ecommerce.db')

        with engine.connect() as conexao:
            conexao.execute(text("""
                CREATE TABLE IF NOT EXISTS produtos_vendas (
                    id_produto INTEGER PRIMARY KEY,
                    nome_produto_padrao TEXT NOT NULL,
                    categoria_padrao TEXT,
                    preco_custo REAL,
                    valor_total_estoque REAL,
                    margem_lucro_estimada REAL,
                    preco_venda_sugerido REAL,
                    avaliacao_cliente REAL,
                    data_processamento TEXT,
                    origem_dado TEXT
                )
            """))
            conexao.commit()

        df.to_sql('produtos_vendas', con=engine, if_exists='replace', index=False)
        logger.info("Sucesso: Dados injetados na tabela relacional 'produtos_vendas'")
        print("✅ Dados armazenados no Banco SQL Local")

        # ==================================================
        # PASSO 2: COMPARTILHAMENTO DE BACKUP NA NUVEM AWS S3
        # ==================================================
        if not AWS_CONFIG["access_key"] or AWS_CONFIG["access_key"] == "SUA_CHAVE_AQUI":
            logger.warning("Upload S3 ignorado: Credenciais ausentes ou padrão no .env")
            print("⚠️ Cloud Storage: Upload S3 ignorado (credenciais não configuradas no arquivo .env)")
        else:
            s3 = boto3.client(
                's3',
                aws_access_key_id=AWS_CONFIG["access_key"],
                aws_secret_access_key=AWS_CONFIG["secret_key"],
                region_name=AWS_CONFIG["region"]
            )

            data_hoje = datetime.now().strftime("%Y%m%d")
            nome_arquivo_s3 = f"vendas_dados_prontos_{data_hoje}.csv"

            s3.upload_file(
                Filename=caminho_local_original,
                Bucket=AWS_CONFIG["bucket"],
                Key=f"ecommerce/dados_processados/{nome_arquivo_s3}"
            )
            logger.info(f"Sucesso: Upload enviado ao S3 -> Bucket: {AWS_CONFIG['bucket']}")
            print("✅ Arquivo de dados replicado com segurança no Amazon S3")

        # ==================================================
        # PASSO 3: GERACÃO DE AGREGAÇÕES PARA NEGÓCIO (Camada Gold)
        # ==================================================
        df_resumo_categoria = df.groupby('categoria_padrao').agg(
            quantidade_produtos=('id_produto', 'count'),
            valor_total_estoque=('valor_total_estoque', 'sum'),
            media_preco_venda=('preco_venda_sugerido', 'mean')
        ).reset_index()

        # Arredondamentos estéticos do relatório executivo
        df_resumo_categoria['valor_total_estoque'] = round(df_resumo_categoria['valor_total_estoque'], 2)
        df_resumo_categoria['media_preco_venda'] = round(df_resumo_categoria['media_preco_venda'], 2)

        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_analitico = os.path.join(PATHS["analytics_data"], f"resumo_por_categoria_{data_hora}.csv")
        
        df_resumo_categoria.to_csv(caminho_analitico, index=False, encoding='utf-8-sig')
        logger.info(f"Sucesso: Matriz de BI sumarizada exportada para {caminho_analitico}")
        print(f"✅ VISÃO ANALÍTICA CONCLUÍDA! Relatório executivo disponível em: {caminho_analitico}")

    except Exception as erro:
        logger.error(f"Erro fatal na rotina de carregamento: {erro}", exc_info=True)
        print("❌ FALHA NA CARGA DOS DADOS. Verifique o arquivo logs/carga.log")
        raise

if __name__ == "__main__":
    try:
        arquivo_silver = buscar_arquivo_mais_recente(PATHS["processed_data"], "vendas_tratado_*.csv")
        df_pronto = pd.read_csv(arquivo_silver)
        carregar_dados(df_pronto, arquivo_silver)
    except Exception as e:
        print(f"Erro ao executar carga isolada: {e}")