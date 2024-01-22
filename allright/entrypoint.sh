#!/bin/sh

echo "Executing entrypoint.sh"

echo "Executing migrate"
python manage.py migrate

exec "$@"