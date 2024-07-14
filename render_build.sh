#!/bin/bash

poetry install --without=dev
poetry run python manage.py migrate
