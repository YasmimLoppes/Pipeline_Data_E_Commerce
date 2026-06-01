# 📊 Pipeline Data E-Commerce

Análise, Ingestão, Qualidade e Governança de Dados de ponta a ponta. Este projeto simula um ambiente real de Engenharia de Dados, consumindo dados de uma API de E-Commerce, aplicando regras de negócio estritas, tratando os dados em conformidade com as boas práticas da arquitetura medalhão (Bronze, Silver, Gold) e distribuindo para armazenamento relacional e nuvem.

---

## 🏗️ Arquitetura do Pipeline

O fluxo de dados foi desenhado seguindo as etapas de um pipeline produtivo moderno:

1. **Ingestão (Camada Bronze):** Script `01_extrair.py` consome a API da Fake Store, tratando resiliência de rede com políticas de retentativas (`max_retries` e `timeout`) e persistindo o histórico bruto em formato CSV com carimbo de data/hora (*timestamp*).
2. **Transformação e Qualidade (Camada Silver):** Script `02_transformar.py` realiza o saneamento dos dados, remove registros nulos em chaves obrigatórias, elimina duplicidades, padroniza strings para análise textual e calcula métricas de negócio (Preço de Custo, Margem de Lucro Estimada e Valor Total de Estoque).
3. **Carga e BI (Camada Gold):** Script `03_carregar.py` injeta os dados estruturados em um banco relacional **SQL (SQLite)**, exporta visões agregadas para relatórios gerenciais executivos e realiza o backup dos dados finais no armazenamento em nuvem **Amazon S3**.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.11
* **Manipulação de Dados:** Pandas / NumPy
* **Conectividade & Nuvem:** Requests / Boto3 (AWS SDK)
* **Banco de Dados:** SQLAlchemy / SQLite
* **Infraestrutura e Isolamento:** Docker / Docker Compose
* **Versionamento & Ambiente:** Git / Python-Dotenv

---

## 📂 Estrutura do Projeto

```text
Pipeline_Data_E_Commerce/
│
├── config/
│   └── __init__.py          # Centralização de variáveis, caminhos e regras de negócio
│
├── data/                    # Camadas de Armazenamento Local (Bronze, Silver, Gold)
│   ├── 01_raw/              # Dados brutos originais da API
│   ├── 02_tratado/          # Dados limpos e sanitizados
│   └── 03_analitico/        # Relatórios prontos para BI
│
├── logs/                    # Arquivos de auditoria de execução por módulo
│
├── scripts/
│   ├── __init__.py          # Fachada de importação inteligente (blindagem de sintaxe)
│   ├── 01_extrair.py        # Motor de ingestão e resiliência de API
│   ├── 02_transformar.py    # Motor de regras de negócio e qualidade
│   ├── 03_carregar.py       # Distribuidor de carga (SQL, S3 e Agregações)
│   └── utils.py             # Funções de suporte (autocriação de pastas e logs)
│
├── .env                     # Variáveis de ambiente e chaves (protegido pelo .gitignore)
├── .gitignore               # Filtro de arquivos locais e sensíveis para o Git
├── Dockerfile               # Configuração da imagem isolada do container
├── docker-compose.yml       # Orquestração do container local
├── main.py                  # Maestro/Orquestrador principal de ponta a ponta
├── requirements.txt         # Bibliotecas e dependências com versões travadas
└── setup.py                 # Empacotamento do projeto