#!/bin/bash

# Remove the database file if it exists
rm -f db.sqlite3

# Finally, run migrations for all other apps
poetry run python manage.py migrate
