#!/bin/bash

./create_venv.sh
source ./.venv/bin/activate
./migrate.sh
