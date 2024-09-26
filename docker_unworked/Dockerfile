FROM python:3.10

# Установка cron, MySQL клиентских инструментов и nano
RUN apt-get update && apt-get install -y cron default-mysql-client nano

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируем файлы проекта в контейнер
COPY .. .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем cron и приложение Django
CMD python manage.py runserver 0.0.0.0:8000
