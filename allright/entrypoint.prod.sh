#!/bin/sh

echo "Executing entrypoint.prod.sh"

echo "Executing migrate"
python manage.py migrate &&

python manage.py collectstatic --no-input &&

exec "$@"