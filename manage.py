#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# # manage.py
# import os
# import sys
# from dotenv import load_dotenv
#
# def main():
#     """Run administrative tasks."""
#     load_dotenv()
#
#     # Устанавливаем настройки по умолчанию
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_v0.settings.base')
#
#     # Получаем значение переменной окружения DJANGO_ENV
#     env = os.getenv('DJANGO_ENV')
#
#     # Устанавливаем соответствующий файл настроек в зависимости от окружения
#     if env == 'production':
#         os.environ['DJANGO_SETTINGS_MODULE'] = 'app_v0.settings.prod'
#     elif env == 'development':
#         os.environ['DJANGO_SETTINGS_MODULE'] = 'app_v0.settings.dev'
#
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
# if __name__ == '__main__':
#     main()
