#!/bin/bash

poetry run python manage.py collectstatic
poetry run python manage.py migrate
