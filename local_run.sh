#!/bin/bash

export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY="django-insecure-abcABC123!@#"

poetry run python manage.py runserver -v 2
