# Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc e força logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema (necessário para alguns pacotes Python)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências do projeto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do código para dentro do container
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor (use gunicorn em produção, mas runserver para dev/teste)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]