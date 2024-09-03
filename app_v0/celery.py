from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings')
celery_app = Celery('app_v0')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'logout_all_users': {
        'task': 'app_v0.tasks.logout_all_users',
        'schedule': crontab(minute="0", hour="2"),  # Запуск каждый день в 2:00
    },
}


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
