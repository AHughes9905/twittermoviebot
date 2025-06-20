FROM python:3.12.9-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps


CMD ["python", "main.py"]