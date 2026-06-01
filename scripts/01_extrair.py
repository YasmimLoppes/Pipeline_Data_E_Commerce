import pandas as pd
import requests
from datetime import datetime
import time
import os
from config import API_CONFIG, PATHS
from scripts.utils import configurar_log

logger = configurar_log("extracao")

def extrair_dados():
    try:
        logger.info("Iniciando Ingestão de Dados (Camada Bronze)")
        resposta = None

        for tentativa in range(API_CONFIG["max_retries"]):
            try:
                resposta = requests.get(
                    API_CONFIG["url"], 
                    timeout=API_CONFIG["timeout"]
                )
                resposta.raise_for_status()
                logger.info(f"Conexão bem sucedida com a API | Tentativa {tentativa+1}")
                break
            except Exception as erro:
                logger.warning(f"Falha na tentativa {tentativa+1}: {erro}")
                if tentativa < API_CONFIG["max_retries"] - 1:
                    time.sleep(3)
                else:
                    raise erro

        if resposta is None:
            raise Exception("Sem resposta válida da API do e-commerce.")

        # Transformação básica da API para Tabela Raw
        dados_brutos = resposta.json()
        df = pd.DataFrame(dados_brutos)

        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_arquivo = os.path.join(PATHS["raw_data"], f"vendas_bruto_{data_hora}.csv")
        
        df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')

        logger.info(f"Extração Concluída | {len(df)} registros armazenados em {caminho_arquivo}")
        print(f"✅ EXTRAÇÃO CONCLUÍDA! Dados originais preservados em: {caminho_arquivo}")
        
        return df

    except Exception as erro:
        logger.error(f"Erro grave na etapa de extração: {erro}", exc_info=True)
        print("❌ FALHA NA EXTRAÇÃO. Verifique o arquivo logs/extracao.log")
        raise

if __name__ == "__main__":
    extrair_dados()