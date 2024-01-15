#!/bin/sh
/web/app/src/manage.py collectstatic --noinput --clear

if [ $ENVIRONMENT = "dev" ]
then
    cd /web/app/src &&
    python -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:80
else
    gunicorn -b 0.0.0.0:80 --chdir /web/app/src homie.wsgi:application
fi 