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
        logger.info("Iniciando Ingestão de Dados da API de Produtos")
        resposta = None

        for tentativa in range(API_CONFIG["max_retries"]):
            try:
                resposta = requests.get(
                    API_CONFIG["url"],
                    timeout=API_CONFIG["timeout"]
                )
                resposta.raise_for_status()
                logger.info(f"Conexão bem sucedida na tentativa {tentativa+1}")
                break

            except Exception as erro:
                logger.warning(f"Falha na tentativa {tentativa+1}: {erro}")
                if tentativa < API_CONFIG["max_retries"] - 1:
                    time.sleep(3)
                else:
                    raise erro

        if resposta is None:
            raise Exception("Sem resposta válida da API após todas as tentativas")

        # Dados capturados e salvos na camada bruta preservando origem
        dados_brutos = resposta.json()
        df_produtos_brutos = pd.DataFrame(dados_brutos)

        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_arquivo = os.path.join(PATHS["raw_data"], f"produtos_brutos_{data_hora}.csv")

        df_produtos_brutos.to_csv(caminho_arquivo, index=False, encoding='utf-8')

        logger.info(f"Extração Concluída | Total de produtos capturados: {len(df_produtos_brutos)}")
        print(f"✅ EXTRAÇÃO CONCLUÍDA! Dados originais salvos na camada BRUTA.")

        return df_produtos_brutos

    except Exception as erro:
        logger.error(f"Erro crítico durante extração: {erro}")
        raise erro