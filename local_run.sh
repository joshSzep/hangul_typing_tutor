#!/bin/bash

source ./.venv/bin/activate

export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY="django-insecure-abcABC123!@#"

python manage.py runserver
