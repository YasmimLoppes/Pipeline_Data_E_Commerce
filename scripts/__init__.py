"""
Pacote de scripts do Pipeline Data E-Commerce
Responsável por: Extração, Transformação, Qualidade e Carga dos dados
Versão: 1.0.0
Desenvolvedora: Yasmim Lopes
"""

import importlib
import sys
import os

# Usamos importlib porque o Python restringe o início numérico em 'import .01_extrair'
_mod_extrair = importlib.import_module('.01_extrair', package=__package__)
_mod_transformar = importlib.import_module('.02_transformar', package=__package__)
_mod_carregar = importlib.import_module('.03_carregar', package=__package__)

extrair_dados = _mod_extrair.extrair_dados
transformar_dados = _mod_transformar.transformar_dados
carregar_dados = _mod_carregar.carregar_dados

def main():
    """Ponto de entrada do console_scripts que chama o maestro na raiz."""
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import main as orquestrador
    orquestrador.executar_pipeline()

__all__ = [
    'extrair_dados',
    'transformar_dados',
    'carregar_dados',
    'main'
]

__version__ = "1.0.0"