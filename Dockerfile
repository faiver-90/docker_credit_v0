# Используем базовый образ Ubuntu
FROM ubuntu:22.04

# Установка основных инструментов и необходимых пакетов для mysqlclient
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    nginx \
    redis-server \
    mysql-client \
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

# Установка pip
RUN pip3 install --upgrade pip

# Создание рабочего каталога
WORKDIR /var/www/motor_finance

# Копирование файла requirements.txt
COPY requirements.txt .
COPY nginx/nginx.conf /etc/nginx/proxy_params
# Установка зависимостей Python
RUN pip3 install -r requirements.txt

# Копирование файлов проекта
COPY . .

# Создание рабочей директории для сокета Gunicorn
RUN mkdir -p /var/www/motor_finance/run && \
    chown -R www-data:www-data /var/www/motor_finance/run

# Установка gunicorn
RUN pip3 install gunicorn

# Запуск сервера
CMD ["gunicorn", "app_v0.wsgi:application", "--bind", "unix:/var/www/motor_finance/run/gunicorn.sock"]
