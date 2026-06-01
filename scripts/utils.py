"""
Funções utilitárias para suporte ao Pipeline Data E-Commerce.
Centraliza a criação de diretórios, logs e varredura inteligente de arquivos.
"""

import os
import glob
import logging
from config import PATHS

def garantir_diretorios():
    """Garante que todas as pastas do projeto existam antes da execução."""
    for nome_pasta, caminho in PATHS.items():
        os.makedirs(caminho, exist_ok=True)

def buscar_arquivo_mais_recente(caminho_pasta, padrao_nome):
    """Busca o arquivo mais recente em uma determinada pasta baseado em um padrão."""
    caminho_busca = os.path.join(caminho_pasta, padrao_nome)
    arquivos = glob.glob(caminho_busca)
    
    if not arquivos:
        raise FileNotFoundError(f"Nenhum arquivo encontrado em '{caminho_pasta}' com o padrão '{padrao_nome}'")
    
    return max(arquivos, key=os.path.getmtime)

def configurar_log(nome_modulo):
    """Configura e retorna um logger customizado para cada etapa do pipeline."""
    garantir_diretorios()  # Assegura a pasta de logs antes do FileHandler
    
    caminho_log = os.path.join(PATHS["logs"], f"{nome_modulo}.log")
    
    logger = logging.getLogger(nome_modulo)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.FileHandler(caminho_log, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger