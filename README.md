# 🛒 Pipeline de Dados E-commerce
**Engenharia de Dados | ETL Completo | Qualidade de Dados | Nuvem | Docker**

> Pipeline completo de extração, transformação e carga de dados de produtos e vendas, seguindo padrões de mercado, regras de negócio e arquitetura profissional. Projeto desenvolvido para portfólio, com foco em qualidade, organização e boas práticas 📊✅

---

## 📋 Sumário
- [📌 Sobre o Projeto](#-sobre-o-projeto)
- [🏗️ Arquitetura do Pipeline](#️-arquitetura-do-pipeline)
- [⚙️ Funcionalidades e Regras de Negócio](#️-funcionalidades-e-regras-de-negócio)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📂 Estrutura Completa do Projeto](#-estrutura-completa-do-projeto)
- [🚀 Como Executar](#-como-executar)
- [📈 Resultados e Saídas](#-resultados-e-saídas)
- [📚 Documentação Completa](#-documentação-completa)
- [👩‍💻 Autora](#-autora)

---

## 🏗️ Arquitetura do Pipeline

```mermaid
graph LR
    API[API de Produtos] -->|Extração| BRONZE[(Camada Bruta)]
    BRONZE -->|Tratamento e Validação| SILVER[(Camada Tratada)]
    SILVER -->|Regras de Negócio e Cálculos| GOLD[(Camada Analítica)]
    GOLD -->|Disponibilização| DB[(Banco de Dados)]
    GOLD -->|Armazenamento| S3[(AWS S3 - Nuvem)]
---

## 📌 Sobre o Projeto

Este projeto é um **Pipeline de Dados ETL (Extração, Transformação e Carga)** completo, desenvolvido com o objetivo de simular fielmente o fluxo real de dados de uma empresa de e-commerce de médio e grande porte, seguindo rigorosamente as melhores práticas, padrões de mercado e conceitos sólidos de Engenharia de Dados.

A proposta principal é coletar dados de produtos, estoque e preços diretamente de uma fonte externa neste caso, uma API pública aplicar regras de negócio validadas, garantir 100% de qualidade, consistência e confiabilidade das informações, e disponibilizar os dados tratados, organizados e estruturados para diferentes finalidades estratégicas: análise de mercado, controle preciso de estoque, definição de preços e margens, relatórios financeiros, auditoria e tomada de decisão segura.

💡 **Um diferencial muito importante:** todo o raciocínio, validações e regras aplicadas foram construídos com base na minha experiência prática anterior, onde atuei diretamente com **Controle de Estoque, Conferência de Valores e Operação de Caixa**. Transformei o conhecimento que tenho do dia a dia de uma loja real em regras técnicas de dados, unindo a visão de negócio com tecnologia de ponta. Sei na prática que **dados errados causam prejuízo, dados duplicados geram contagem errada e dados desorganizados não servem para nada**, e foi exatamente para evitar isso que cada etapa desse pipeline foi pensada e estruturada.

Todo o fluxo foi construído pensando em **escalabilidade, segurança, governança e manutenção**:

- ✅ **Arquitetura de Camadas (Medalhão):** Os dados passam por 3 estágios bem definidos e separados *Bruto → Tratado → Analítico*. Isso garante a preservação total da informação original (nunca alteramos o dado bruto), permite evolução controlada dos dados e deixa tudo organizado por etapa de processamento, facilitando manutenção e auditoria.

- ✅ **Qualidade de Dados como prioridade:** Todas as etapas contam com validações rigorosas: remoção de duplicatas, descarte de registros incompletos, validação de intervalos de valores, padronização de textos e categorias. A regra principal aqui é: **só informação confiável e correta pode chegar até a análise final**.

- ✅ **Padrões Profissionais de Mercado:** Utilização de contêineres (Docker) para garantir que o projeto rode de forma idêntica em qualquer máquina, independente de sistema operacional ou versões instaladas; armazenamento em nuvem (AWS S3) seguindo o que é adotado pelas grandes empresas; e organização modular do código, permitindo que o projeto cresça e seja adaptado para novas necessidades sem bagunça.

- ✅ **Rastreabilidade Total:** Cada arquivo gerado tem data e hora de criação; cada linha de dado tratado carrega consigo informações de origem, data/hora de processamento e histórico de alterações. Isso é essencial para responder, a qualquer momento: *“De onde veio esse dado? Quando foi processado? Quais regras foram aplicadas?”*, requisito básico para conformidade e confiança na informação.

- ✅ **Valor Agregado:** Não apenas coletamos e guardamos dados brutos, mas transformamos eles em informação útil. Calculamos valores totais de estoque, margens de lucro, preços sugeridos e resumos estratégicos, entregando diretamente o que o gestor ou dono do negócio realmente precisa saber.

Além de ser um pipeline funcional, testado e completo, este projeto serve como demonstração prática de domínio das ferramentas, conceitos, arquitetura e processos que são exigidos no dia a dia de um Engenheiro de Dados, mostrando desde a extração da informação crua até a entrega final de inteligência para o negócio.

---

## 🏗️ Arquitetura do Pipeline

O pipeline segue a arquitetura de medalhão, dividida em três camadas principais: **Bruto, Tratado e Analítico**, garantindo segurança, qualidade e evolução dos dados ao longo do processo.

> Fluxo: Extração → Validação e Tratamento → Transformação e Cálculos → Disponibilização

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

Ferramenta	| Propósito
--- | ---
🐍 Python 3.11+ | Linguagem principal, manipulação e automação
🐼 Pandas / NumPy | Processamento, limpeza e cálculo de dados em larga escala
🗄️ SQLAlchemy / SQLite | Armazenamento relacional, consultas e persistência
☁️ AWS S3 (boto3) | Armazenamento seguro em nuvem, padrão de mercado
🐳 Docker / Docker Compose | Ambiente isolado, execução igual em qualquer máquina
🔐 python-dotenv | Segurança: armazena chaves e senhas fora do código
📝 Logging | Auditoria, histórico e rastreabilidade total
📦 Git / GitHub | Controle de versão e repositório

📌 *Explicação detalhada: [`docs/TECNOLOGIAS_USADAS.md`](docs/TECNOLOGIAS_USADAS.md)*

---

👩‍💻 Autora
Yasmim Lopes Engenheira de Dados apaixonada por transformar dados brutos em inteligência.