#!/bin/sh
gunicorn -b 0.0.0.0:80 --chdir /web/app/src homie.wsgi:application