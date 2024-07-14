#!/bin/bash

poetry install --without=dev
poetry run python manage.py collectstatic
poetry run python manage.py migrate
