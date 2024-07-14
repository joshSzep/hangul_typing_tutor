#!/bin/bash

source ./.venv/bin/activate
gunicorn hangul_tutor.wsgi:application --bind 0.0.0.0:$PORT
