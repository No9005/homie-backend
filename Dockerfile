FROM python:3.11-slim-bookworm

RUN apt update && apt upgrade

RUN python -m pip install --upgrade pip

RUN mkdir -p /web/app

COPY ./requirements.txt /web/app/requirements.txt
RUN pip install -r /web/app/requirements.txt

COPY ./src /web/app/src

ENTRYPOINT ["/bin/bash", "/web/app/entrypoint/start.sh"]