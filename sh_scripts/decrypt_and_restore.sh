#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <backup_filename>"
  exit 1
fi

BACKUP_FILENAME=$1

# Загрузка переменных окружения
source .env

# Параметры базы данных
DB_NAME=$NAME
DB_USER=$USER_MYSQL_SERVE
DB_PASS=$PASSWORD_MYSQL_SERVE
BACKUP_DIR="/var/www/motor_finance/backup_mysql/"
BACKUP_FILE="${BACKUP_FILENAME}.sql.gpg"

# Лог файл
LOG_FILE="/var/log/decrypt_and_restore.log"

# Функция логирования
log() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

log "Начало процесса восстановления базы данных"

# Шаг 1: Расшифровка резервной копии с запросом пароля
log "Расшифровка файла $BACKUP_FILE"
DECRYPTED_FILE="$BACKUP_DIR/${BACKUP_FILENAME}.sql"
if gpg --decrypt "$BACKUP_DIR/$BACKUP_FILE" > "$DECRYPTED_FILE"; then
  log "Расшифровка успешна: $DECRYPTED_FILE"
else
  log "Ошибка расшифровки файла $BACKUP_FILE"
  exit 1
fi

# Проверьте, что файл был создан
if [ -f "$DECRYPTED_FILE" ]; then
  log "Файл расшифрован и существует: $DECRYPTED_FILE"
else
  log "Файл не был создан: $DECRYPTED_FILE"
  exit 1
fi

# Шаг 2: Восстановление базы данных
log "Восстановление базы данных $DB_NAME из файла $DECRYPTED_FILE"
if mysql -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" < "$DECRYPTED_FILE"; then
  log "Восстановление базы данных успешно"
else
  log "Ошибка восстановления базы данных"
  rm "$DECRYPTED_FILE"
  exit 1
fi

log "Процесс восстановления завершен"
