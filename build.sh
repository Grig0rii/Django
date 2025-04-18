#!/usr/bin/env bash
# exit on error
set -o errexit

# Обновление pip
python -m pip install --upgrade pip

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate

python create_superuser.py 