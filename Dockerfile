# Используем официальный образ Python
FROM python:3.10

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    nginx \
    redis-server \
    default-mysql-client \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    wget \
    git \
    vim \
    nano \
    sudo \
    unzip \
    htop \
    && apt-get clean

# Установка рабочей директории
WORKDIR /var/www/motor_finance

# Копируем файлы проекта в контейнер
COPY . /var/www/motor_finance

# Установка Python зависимостей
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем скрипт запуска Gunicorn и делаем его исполняемым
COPY ./gunicorn_start.sh /var/www/motor_finance/gunicorn_start.sh
RUN chmod +x /var/www/motor_finance/gunicorn_start.sh

# Запуск Django через Gunicorn
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "app_v0.wsgi:application"]
#CMD ["./gunicorn_start.sh"]
