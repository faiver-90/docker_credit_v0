#!/bin/bash

# Проверка наличия аргумента
if [ -z "$1" ]; then
  echo "Ошибка: Не указан хэш коммита."
  echo "Использование: $0 <short_commit_hash>"
  exit 1
fi

# Получение короткого хэша из аргумента
short_commit_hash=$1

# Определение текущей ветки
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Откат текущей ветки до указанного хэша
git reset --hard $short_commit_hash

# Проверка результата команды
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось откатить ветку до коммита $short_commit_hash."
  exit 1
fi

echo "Ветка успешно откатилась до коммита $short_commit_hash."

# Форсированная отправка изменений в удаленный репозиторий
git push origin $current_branch --force

# Проверка результата команды
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось отправить изменения в удаленный репозиторий."
  exit 1
fi

echo "Изменения успешно отправлены в удаленный репозиторий."
