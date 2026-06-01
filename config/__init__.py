"""
Módulo de configurações do Pipeline
Centraliza caminhos, variáveis e parâmetros
"""
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# 📌 CAMINHOS DO SISTEMA - Definidos uma vez só
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

PATHS = {
    "raw_data": os.path.join(PROJECT_ROOT, "data", "01_raw"),
    "processed_data": os.path.join(PROJECT_ROOT, "data", "02_tratado"),
    "analytics_data": os.path.join(PROJECT_ROOT, "data", "03_analitico"),
    "logs": os.path.join(PROJECT_ROOT, "logs")
}

# 📌 CONFIGURAÇÕES DA API
API_CONFIG = {
    "url": "https://fakestoreapi.com/products",
    "timeout": 15,
    "max_retries": 3
}

# 📌 CONFIGURAÇÕES AWS
AWS_CONFIG = {
    "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
    "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "region": os.getenv("AWS_REGION", "us-east-1"),
    "bucket": os.getenv("BUCKET_NAME")
}

# 📌 REGRAS DE NEGÓCIO
BUSINESS_RULES = {
    "min_price": 0.01,
    "max_price": 10000.00,
    "estoque_padrao": 50,
    "margem_lucro": 0.35,
    "campos_obrigatorios": ["id", "title", "price", "category"]
}