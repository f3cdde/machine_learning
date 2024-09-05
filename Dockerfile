# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . .

# Comando para executar o script de machine learning
CMD ["python", "src/wine_quality.py"]
