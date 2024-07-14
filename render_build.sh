#!/bin/bash

poetry install
source ./.venv/bin/activate
./migrate.sh
