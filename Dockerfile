FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt