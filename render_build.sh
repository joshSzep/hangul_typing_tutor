#!/bin/bash

poetry install --without=dev
python run python manage.py collectstatic
poetry run python manage.py migrate
