"""
ASGI config for app_v0 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings')

application = get_asgi_application()

# import os
# from django.core.wsgi import get_wsgi_application
#
# # Устанавливаем настройки по умолчанию
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings.base')
#
# # Получаем значение переменной окружения DJANGO_ENV
# env = os.getenv('DJANGO_ENV')
#
# # Устанавливаем соответствующий файл настроек в зависимости от окружения
# if env == 'production':
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'app_v0.settings.prod'
# elif env == 'development':
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'app_v0.settings.dev'
#
# application = get_wsgi_application()