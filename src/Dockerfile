FROM python:3.9.4-alpine

WORKDIR /FastAPI/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /FastAPI/src/app/requirements.txt

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /FastAPI/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /FastAPI/src/app/