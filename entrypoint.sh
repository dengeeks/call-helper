#!/bin/sh

if [ "$PG_ENGINE" = "django.db.backends.postgresql_psycopg2" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
