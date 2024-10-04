#!/usr/bin/env bash

NAME="motor_finance"
DJANGODIR=/var/www/motor_finance
#SOCKFILE=/var/www/motor_finance/run/gunicorn.sock

USER=faiver90
GROUP=www-data
NUM_WORKERS=2
DJANGO_SETTINGS_MODULE=app_v0.settings
DJANGO_WSGI_MODULE=app_v0.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --worker-class sync \
  --max-requests 1000 \
  --access-logfile /var/log/gunicorn/access.log \
  --error-logfile /var/log/gunicorn/error.log \
  --log-level debug \
  --max-requests-jitter 100 \
  --worker-connections 1000 \
  --user=$USER --group=$GROUP \
  --bind=0.0.0.0:8000 \
  --log-level=debug \
