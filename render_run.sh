#!/bin/bash

poetry run gunicorn hangul_tutor.wsgi:application --bind 0.0.0.0:$PORT
