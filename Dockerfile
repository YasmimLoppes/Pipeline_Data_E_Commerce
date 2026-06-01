FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto
COPY . .

# Define variável de ambiente para o Python localizar as pastas config e scripts
ENV PYTHONPATH=/app

# Comando padrão: Roda o pipeline completo de ponta a ponta
CMD ["python", "main.py"]