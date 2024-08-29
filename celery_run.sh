#!/bin/bash

echo "Запуск Celery..."

celery -A app_v0 worker --loglevel=info
# celery -A app_v0 worker --loglevel=info --pool=solo
# celery -A app_v0 worker --loglevel=info --pool=prefork
