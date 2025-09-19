FROM python:3.10-slim

WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fonte
COPY src/ src/

# Criar diretórios de saída
RUN mkdir -p src/csv src/figures

CMD ["python", "src/run_all.py"]
