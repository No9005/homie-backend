#!/bin/sh
/web/app/src/manage.py collectstatic --noinput --clear
/web/app/src/manage.py migrate

gunicorn -b 0.0.0.0:80 --chdir /web/app/src homie.wsgi:application