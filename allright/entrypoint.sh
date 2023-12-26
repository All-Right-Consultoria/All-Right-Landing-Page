#!/bin/sh

echo "Executing entrypoint.sh"

echo "Executing flush"
python manage.py flush --no-input

echo "Executing migrate"
python manage.py migrate

exec "$@"