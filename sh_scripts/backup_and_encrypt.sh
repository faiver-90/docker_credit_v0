#!/bin/bash

# Загрузка переменных окружения
source /var/www/motor_finance/.env

# Параметры базы данных
DB_NAME=$NAME
DB_USER=$USER_MYSQL_SERVE
DB_PASS=$PASSWORD_MYSQL_SERVE
BACKUP_DIR="/var/www/motor_finance/backup_mysql/"
DATE=$(date +"%Y%m%d%H%M")

# Имя файла резервной копии
BACKUP_FILE="${DB_NAME}_${DATE}.sql"

# Лог файл
LOG_FILE="/var/log/backup_and_encrypt.log"

# Функция логирования
log() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

log "Начало процесса резервного копирования базы данных"

# Шаг 1: Резервное копирование базы данных
log "Создание резервной копии базы данных $DB_NAME"
if mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/$BACKUP_FILE"; then
  log "Резервное копирование успешно: $BACKUP_FILE"
else
  log "Ошибка резервного копирования базы данных"
  exit 1
fi

# Шаг 2: Шифрование резервной копии
log "Шифрование файла резервной копии $BACKUP_FILE"
if gpg --batch --yes --encrypt --recipient faiver90@mail.ru "$BACKUP_DIR/$BACKUP_FILE"; then
  log "Шифрование успешно"
else
  log "Ошибка шифрования файла резервной копии"
  rm "$BACKUP_DIR/$BACKUP_FILE"
  exit 1
fi

# Удаление исходного файла резервной копии
log "Удаление исходного файла резервной копии $BACKUP_FILE"
rm "$BACKUP_DIR/$BACKUP_FILE"

# Удаление старых зашифрованных резервных копий (старше 365 дней)
log "Удаление старых зашифрованных резервных копий (старше 365 дней)"
find "$BACKUP_DIR" -type f -name "*.sql.gpg" -mtime +365 -exec rm {} \;

log "Процесс резервного копирования завершен"
