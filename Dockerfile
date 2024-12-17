FROM python:3.12

ENV HTTP_PROXY=http://proxy-enclave.altera.com:912
ENV HTTPS_PROXY=http://proxy-enclave.altera.com:912

RUN apt-get update && apt-get install -y wget curl

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:3000", "main:app"]

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://0.0.0.0:3000/healthcheck || exit 1
