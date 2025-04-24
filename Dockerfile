FROM python:3.13.3-alpine

RUN apk add --no-cache build-base libffi-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY domain/ ./domain
COPY src/ ./src
COPY app.py .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
