from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Задайте переменную окружения для настроек Django
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings')

# Создайте экземпляр Celery
celery_app = Celery('app_v0')

# Используйте конфигурацию из настроек Django, используя префикс 'CELERY'
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в ваших приложениях Django
celery_app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'sample_task': {
        'task': 'app_v0.tasks.sample_task',
        'schedule': crontab(minute='*'),  # Каждую минуту
    },
}
@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
