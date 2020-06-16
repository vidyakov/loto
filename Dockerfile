FROM python:latest

WORKDIR /app

COPY loto/requirements.txt .
RUN pip install -r requirements.txt

COPY loto/classes ./classes
COPY loto/main.py ./
