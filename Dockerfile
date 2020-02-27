FROM python:3.8.0-alpine
LABEL Maintainer="Thiago Beviláqua" Name=rispar Version=0.0.1
RUN mkdir /app
COPY . /app
ENV PYTHONUNBUFFERED 1
WORKDIR /app
