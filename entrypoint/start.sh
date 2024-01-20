#!/bin/sh
/web/app/src/manage.py collectstatic --noinput --clear
/web/app/src/manage.py migrate

cd /web/app/src &&
python -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:80
