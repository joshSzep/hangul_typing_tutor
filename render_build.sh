#!/bin/bash

env use 3.12
./create_venv.sh
source ./.venv/bin/activate
./migrate.sh
