import pandas as pd
from datetime import datetime
import os
from config import PATHS, AWS_CONFIG
from scripts.utils import configurar_log
from scripts.aws_utils import enviar_para_s3
from scripts.database import carregar_no_banco

logger = configurar_log("carregamento")

def carregar_dados(df_produtos_validados, df_analitico):
    try:
        logger.info("Iniciando etapa de carregamento e disponibilização dos dados")

        # Salvando arquivo final consolidado
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_final = os.path.join(PATHS["final_data"], f"produtos_consolidados_{data_hora}.csv")
        df_produtos_validados.to_csv(caminho_final, index=False, encoding='utf-8')
        logger.info(f"Arquivo consolidado salvo em: {caminho_final}")

        # Envio para a nuvem AWS S3 - armazenamento seguro e escalável
        if AWS_CONFIG["enabled"]:
            logger.info("Enviando arquivos para a nuvem AWS S3")
            enviar_para_s3(caminho_final, AWS_CONFIG["bucket_name"], f"produtos/produtos_consolidados_{data_hora}.csv")
            enviar_para_s3(os.path.join(PATHS["analytics_data"], f"resumo_produtos_{data_hora}.csv"), 
                           AWS_CONFIG["bucket_name"], 
                           f"analitico/resumo_produtos_{data_hora}.csv")

        # Carregamento no Banco de Dados SQL para consultas rápidas
        logger.info("Carregando dados estruturados no Banco SQL")
        carregar_no_banco(df_produtos_validados, "produtos")
        carregar_no_banco(df_analitico, "resumo_categorias")

        logger.info("Carregamento finalizado com sucesso! Dados disponíveis para uso.")
        print(f"✅ CARREGAMENTO CONCLUÍDO! Tudo salvo na nuvem e no banco de dados.")

        return True

    except Exception as erro:
        logger.error(f"Erro durante etapa de carregamento: {erro}")
        raise erro