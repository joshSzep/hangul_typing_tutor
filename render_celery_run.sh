#!/bin/bash

poetry run celery -A hangul_tutor worker -l info
