#!/bin/bash
DJANGO_SUPERUSER_EMAIL:-"admin"
cd /app/
/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createadmin
