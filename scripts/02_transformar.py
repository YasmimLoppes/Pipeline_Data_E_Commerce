import pandas as pd
import numpy as np
from datetime import datetime
import os
from config import PATHS
from scripts.utils import configurar_log

logger = configurar_log("transformacao")

def transformar_dados(df_produtos_brutos):
    try:
        logger.info("Iniciando processo de validação e transformação dos dados")

        # Trabalha sobre cópia preservando dados originais
        df_produtos = df_produtos_brutos.copy()

        # Remove registros sem dados essenciais para operação
        campos_obrigatorios = ['title', 'price', 'category']
        df_produtos_validados = df_produtos.dropna(subset=campos_obrigatorios).copy()
        logger.info(f"Registros após limpeza de dados obrigatórios: {len(df_produtos_validados)}")

        # Validação de valor: faixa de preço praticada no mercado
        df_produtos_validados = df_produtos_validados[
            (df_produtos_validados['price'] > 0.01) & 
            (df_produtos_validados['price'] <= 10000.00)
        ].copy()
        logger.info(f"Registros após validação de preço: {len(df_produtos_validados)}")

        # Padronização de texto e categorias
        df_produtos_validados['category'] = df_produtos_validados['category'].str.strip().str.title()
        df_produtos_validados['title'] = df_produtos_validados['title'].str.strip()

        # Cálculos baseados em prática de mercado e gestão de estoque
        df_produtos_validados['valor_total_estoque'] = df_produtos_validados['price'] * 100
        df_produtos_validados['margem_lucro'] = df_produtos_validados['price'] * 0.30
        df_produtos_validados['preco_venda_sugerido'] = df_produtos_validados['price'] * 1.30

        # Dados de auditoria e rastreabilidade
        data_processamento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df_produtos_validados['data_processamento'] = data_processamento
        df_produtos_validados['origem_dado'] = "API - Dados Brutos"

        # Salvando camada TRATADA
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_tratado = os.path.join(PATHS["processed_data"], f"produtos_tratados_{data_hora}.csv")
        df_produtos_validados.to_csv(caminho_tratado, index=False, encoding='utf-8')

        # Preparando visão para camada ANALÍTICA
        df_analitico = df_produtos_validados.groupby('category').agg(
            quantidade_produtos = ('id', 'count'),
            valor_total_estoque = ('valor_total_estoque', 'sum'),
            preco_medio = ('price', 'mean'),
            margem_total_estimada = ('margem_lucro', 'sum')
        ).reset_index()

        # Salvando camada ANALÍTICA
        caminho_analitico = os.path.join(PATHS["analytics_data"], f"resumo_produtos_{data_hora}.csv")
        df_analitico.to_csv(caminho_analitico, index=False, encoding='utf-8')

        logger.info("Transformação concluída | Camadas Tratada e Analítica geradas")
        print(f"✅ TRANSFORMAÇÃO CONCLUÍDA! Dados limpos, validados e calculados.")

        return df_produtos_validados, df_analitico

    except Exception as erro:
        logger.error(f"Erro durante transformação: {erro}")
        raise erro