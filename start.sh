#!/usr/bin/env bash

python backend/manage.py migrate
python backend/manage.py collectstatic --noinput
gunicorn config.wsgi:application
