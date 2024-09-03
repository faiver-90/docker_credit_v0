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
    'logout_all_users': {
        'task': 'app_v0.tasks.logout_all_users',
        'schedule': crontab(minute="0", hour="2"),  # Запуск каждый день в 2:00
    },
}


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
