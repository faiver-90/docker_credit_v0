#!/bin/bash

# Определение текущей ветки
CURRENT_BRANCH=$(git branch --show-current)

if [ -z "$CURRENT_BRANCH" ]; then
  echo "Ошибка: Не удалось определить текущую ветку."
  exit 1
fi

# Переключаемся на основную ветку
echo "Переключаемся на основную ветку..."
git checkout main
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось переключиться на основную ветку."
  exit 1
fi

# Обновляем основную ветку
echo "Обновляем основную ветку..."
git pull origin main
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось обновить основную ветку."
  exit 1
fi

# Сливаем текущую ветку с основной
echo "Сливаем текущую ветку $CURRENT_BRANCH с основной..."
git merge $CURRENT_BRANCH
if [ $? -ne 0 ]; then
  echo "Ошибка: Слияние завершилось с конфликтами. Разрешите конфликты вручную."
  exit 1
fi

# Отправляем изменения в удаленный репозиторий
echo "Отправляем изменения в удаленный репозиторий..."
git push origin main
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось отправить изменения в удаленный репозиторий."
  exit 1
fi

# Возвращаемся в исходную ветку
echo "Возвращаемся в исходную ветку $CURRENT_BRANCH..."
git checkout $CURRENT_BRANCH
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось переключиться обратно на ветку $CURRENT_BRANCH."
  exit 1
fi

echo "Слияние завершено успешно и возвращено в ветку $CURRENT_BRANCH."
