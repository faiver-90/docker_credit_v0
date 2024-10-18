@echo off
setlocal

echo Останавливаю и удаляю контейнеры...
docker-compose down

echo Удаляю контейнеры и образы...
docker container prune -f
docker image prune -a -f

echo Собираю проект заново...
docker-compose up --build -d

echo Проект успешно пересобран и запущен.

endlocal
