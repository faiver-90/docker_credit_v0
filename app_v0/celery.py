from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# from django_celery_beat.models import PeriodicTask, IntervalSchedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings')
celery_app = Celery('app_v0')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
celery_app.conf.beat_scheduler = 'django_celery_beat.scheduler:DatabaseScheduler'


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
