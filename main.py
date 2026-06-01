import sys
import os
import logging

# Garante que a raiz do projeto está no caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# ✅ IMPORTAÇÃO CORRIGIDA (Sem os números que travam o Python)
from scripts import extrair_dados, transformar_dados, carregar_dados  # type: ignore
from scripts.utils import garantir_diretorios, configurar_log, buscar_arquivo_mais_recente  # type: ignore
from config import PATHS  # type: ignore

logger = configurar_log("orquestrador_main")

def executar_pipeline():
    print("🚀 INICIANDO PIPELINE DATA E-COMMERCE...")
    logger.info("--- Nova execução de pipeline iniciada ---")
    
    try:
        # Passo 0: Preparar terreno
        garantir_diretorios()
        
        # Passo 1: Extração
        print("\n=== PASSO 1: EXTRAÇÃO ===")
        df_bruto = extrair_dados()
        
        # Passo 2: Transformação
        print("\n=== PASSO 2: TRANSFORMAÇÃO E QUALIDADE ===")
        df_tratado = transformar_dados(df_bruto)
        
        # Passo 3: Carga
        print("\n=== PASSO 3: CARGA (SQL & NUVEM) ===")
        arquivo_silver = buscar_arquivo_mais_recente(PATHS["processed_data"], "vendas_tratado_*.csv")
        carregar_dados(df_tratado, arquivo_silver)
        
        print("\n🏆 PIPELINE EXECUTADO COM SUCESSO COMPLETO!")
        logger.info("Pipeline finalizado com sucesso absoluto de ponta a ponta.")
        
    except Exception as erro:
        print(f"\n❌ CRÍTICO: O Pipeline falhou durante a execução. Erro: {erro}")
        logger.critical(f"Falha na orquestração do pipeline: {erro}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    executar_pipeline()