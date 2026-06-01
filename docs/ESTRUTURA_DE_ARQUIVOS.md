# 📂 DOCUMENTAÇÃO: ESTRUTURA E ARQUITETURA DE ARQUIVOS

Neste documento explico detalhadamente **para que serve cada arquivo e pasta** do projeto, e o motivo de eu ter organizado dessa forma, seguindo as melhores práticas de Engenharia de Dados e Software.

---

## 📁 RAIZ DO PROJETO (Pasta Principal)

### 📄 `README.md`
**O que é:** Arquivo principal de apresentação.
**Para que serve:** É a primeira coisa que aparece no GitHub. Contém o resumo do projeto, o propósito, como executar e os resultados principais.
**📌 Por que fiz assim:** Deixo ele limpo e objetivo, para qualquer pessoa entender o projeto rapidamente sem precisar ler tudo.

### 📄 `.env`
**O que é:** Arquivo de variáveis de ambiente.
**Para que serve:** Guarda segredos, chaves de acesso e configurações pessoais. **Esse arquivo NÃO SOBE para o GitHub.**
**📌 Por que fiz assim:** Segurança! Nunca deixamos senhas ou chaves dentro do código.

### 📄 `.gitignore`
**O que é:** Arquivo de regras para o Git.
**Para que serve:** Diz para o Git quais arquivos/pastas ele deve ignorar.
**📌 Por que fiz assim:** Evita que arquivos desnecessários ou confidenciais sejam enviados.

### 📄 `requirements.txt`
**O que é:** Lista de dependências.
**Para que serve:** Lista todas as bibliotecas e versões exatas que o projeto precisa.
**📌 Por que fiz assim:** Padronização. Garante que rode igual em qualquer máquina.

### 📄 `setup.py`
**O que é:** Arquivo de configuração de pacote Python.
**Para que serve:** Define nome, versão e dependências do projeto.
**📌 Por que fiz assim:** Profissionalismo. Estrutura o projeto como um pacote oficial.

### 📄 `Dockerfile`
**O que é:** Arquivo de definição de imagem Docker.
**Para que serve:** Instruções para criar um ambiente idêntico ao meu dentro de um contêiner.
**📌 Por que fiz assim:** "Uma vez construído, roda em qualquer lugar".

### 📄 `docker-compose.yml`
**O que é:** Arquivo de orquestração Docker.
**Para que serve:** Facilita o uso do Docker com apenas um comando.
**📌 Por que fiz assim:** Deixa o uso do projeto muito mais simples.

---

## 📁 PASTA `scripts/`

### 📄 `__init__.py`
**O que é:** Arquivo especial do Python.
**Para que serve:** Transforma a pasta em um pacote importável.
**📌 Por que fiz assim:** Organização e limpeza do sistema.

### 📄 `01_extrair.py` / `02_transformar.py` / `03_carregar.py`
**O que são:** Os passos principais do pipeline.
**Para que servem:** Cada um com sua responsabilidade única (um arquivo, uma função).
**📌 Por que fiz assim:** Facilita a manutenção e evita erros.

### 📄 `utils.py`
**O que é:** Funções auxiliares.
**Para que serve:** Guarda funções usadas em vários lugares (log, pastas).
**📌 Por que fiz assim:** Não repetir código (DRY).

---

## 📁 PASTA `config/`

### 📄 `__init__.py`
**O que é:** Centralizador de configurações.
**Para que serve:** Regras de negócio, margens e caminhos.
**📌 Por que fiz assim:** Altero valores em um único lugar e o sistema inteiro reflete a mudança.

---

## 📁 OUTRAS PASTAS

### 📂 `data/`
Arquitetura de Medalhão (raw, tratado, analitico).
**📌 Por que fiz assim:** Preservação do dado original e organização.

### 📂 `logs/`
Histórico de execução.
**📌 Por que fiz assim:** Auditoria e rastreabilidade.

### 📂 `tests/`
Testes automatizados.
**📌 Por que fiz assim:** Garante que o futuro não quebre o presente.