FROM python:3.9.9 AS development_build

ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN apt update \
    && apt install gettext -y

WORKDIR /usr/src/app

RUN pip install poetry

COPY . .

RUN poetry install

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

FROM development_build AS production_build
