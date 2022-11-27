#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate
celery -A config worker --pool=solo -l info
celery -A config beat -l info

uwsgi --socket :9000 --workers 4 --master --enable-threads --module config.wsgi