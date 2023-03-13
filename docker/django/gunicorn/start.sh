#!/usr/bin/env bash

# Using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production"
echo "DJANGO_ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" != 'production' ]; then
  echo 'Error: DJANGO_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_ENV

# Run python specific scripts:
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
echo "Starting gunicorn..."
gunicorn --config python:docker.django.gunicorn.config server.wsgi
