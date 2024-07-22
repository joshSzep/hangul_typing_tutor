#!/bin/bash

poetry run celery -A hangul_tutor worker -l error -D
poetry run gunicorn hangul_tutor.wsgi:application --bind 0.0.0.0:$PORT
