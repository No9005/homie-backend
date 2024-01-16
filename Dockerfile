FROM python:3.11-slim-bookworm

ARG user=appuser

RUN apt update && apt upgrade
RUN python -m pip install --upgrade pip

RUN mkdir -p /web/app

RUN groupadd -g 999 ${user}
RUN useradd -r -u 999 -g ${user} --create-home ${user}
USER ${user}

COPY ./requirements.txt /web/app/requirements.txt
RUN pip install -r /web/app/requirements.txt

COPY ./src /web/app/src

WORKDIR /web/app

ENTRYPOINT ["/bin/bash", "/web/app/entrypoint/start.sh"]