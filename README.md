# 🛒 Pipeline de Dados — E-commerce
**Engenharia de Dados | ETL Completo | Qualidade de Dados | Nuvem | Docker**

> Pipeline completo de extração, transformação e carga de dados de produtos e vendas, seguindo padrões de mercado, regras de negócio e arquitetura profissional. Projeto desenvolvido para portfólio, com foco em qualidade, organização e boas práticas 📊✅

---

## 📋 Sumário
- [📌 Sobre o Projeto](#-sobre-o-projeto)
- [⚙️ Funcionalidades e Regras de Negócio](#️-funcionalidades-e-regras-de-negócio)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📂 Estrutura Completa do Projeto](#-estrutura-completa-do-projeto)
- [🚀 Como Executar](#-como-executar)
- [📈 Resultados e Saídas](#-resultados-e-saídas)
- [📚 Documentação Completa](#-documentação-completa)
- [👩‍💻 Autora](#-autora)

---

## 📌 Sobre o Projeto
Este projeto é um **Pipeline de Dados ETL (Extração, Transformação e Carga)** completo, construído para simular o fluxo real de dados de uma empresa de e-commerce.

O objetivo principal é coletar dados de produtos de uma API pública, aplicar regras de negócio, garantir qualidade das informações e disponibilizar os dados prontos para análise, estoque, precificação e tomada de decisão.

Foi desenvolvido seguindo conceitos de **Arquitetura de Camadas**, **Governança de Dados**, **Contêineres** e **Segurança**, tudo organizado como projeto profissional de Engenharia de Dados.

---

## ⚙️ Funcionalidades e Regras de Negócio
Todas as etapas seguem regras definidas com base em operações reais de varejo e estoque:

✅ **Extração Confiável**
- Coleta dados da API [Fake Store API](https://fakestoreapi.com/products)
- Sistema de tentativas e tratamento de falhas
- Dados brutos salvos com data/hora, **nunca alterados** (imutabilidade)

✅ **Qualidade e Validação**
- Remoção de registros duplicados
- Descarte de dados incompletos (sem ID, nome, preço ou categoria)
- Validação de valores: preço entre R$ 0,01 e R$ 10.000,00
- Padronização de textos e categorias

✅ **Transformação e Cálculos Estratégicos**
- Cálculo de valor total do estoque
- Definição de margem de lucro e preço de venda sugerido
- Criação de colunas de auditoria: data de processamento e origem do dado
- Geração de visão analítica: resumo por categoria, média de preços e valores totais

✅ **Armazenamento e Carga**
- Salvamento em camadas: **Bruto → Tratado → Analítico**
- Carga automática em Banco de Dados Relacional (SQLite)
- Envio seguro para armazenamento em nuvem (AWS S3)
- Registro completo de tudo que acontece em arquivos de Log

📌 *Detalhes completos de todas as regras: [`docs/REGRAS_DE_NEGOCIO.md`](docs/REGRAS_DE_NEGOCIO.md)*

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Propósito |
|---|---|
| 🐍 **Python 3.11+** | Linguagem principal, manipulação e automação |
| 🐼 **Pandas / NumPy** | Processamento, limpeza e cálculo de dados em larga escala |
| 🗄️ **SQLAlchemy / SQLite** | Armazenamento relacional, consultas e persistência |
| ☁️ **AWS S3 (boto3)** | Armazenamento seguro em nuvem, padrão de mercado |
| 🐳 **Docker / Docker Compose** | Ambiente isolado, execução igual em qualquer máquina |
| 🔐 **python-dotenv** | Segurança: armazena chaves e senhas fora do código |
| 📝 **Logging** | Auditoria, histórico e rastreabilidade total |
| 📦 **Git / GitHub** | Controle de versão e repositório |

📌 *Explicação detalhada: [`docs/TECNOLOGIAS_USADAS.md`](docs/TECNOLOGIAS_USADAS.md)*

---

## 📂 Estrutura Completa do Projeto
Organização modular, fácil de manter e escalar:

```text
Pipeline Data E-Commerce/
├── config/              # Centralizador de regras e configurações
├── data/                # Armazenamento: raw, tratado, analitico
├── docs/                # Documentação detalhada
├── logs/                # Histórico de execução
├── scripts/             # Código fonte do ETL (extrair, transformar, carregar)
├── tests/               # Testes automatizados
├── .env                 # Variáveis de ambiente (sensíveis)
├── .gitignore           # Regras de exclusão do Git
├── docker-compose.yml   # Orquestração
├── Dockerfile           # Configuração de imagem
├── main.py              # Ponto de entrada do pipeline
├── requirements.txt     # Dependências do projeto
└── setup.py             # Configuração de pacote Python

## 👩‍💻 Autora
**Yasmim Lopes**
*Engenheira de Dados apaixonada por transformar dados brutos em inteligência.*