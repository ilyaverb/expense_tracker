FROM python:3.10-alpine3.16

LABEL maintainer="verbiloilyaa@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src/requirements.txt /requirements.txt
COPY ./src ./app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache \
        curl gcc postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps

WORKDIR /app/

EXPOSE 8000

ENV PATH="/py/bin/:$PATH"