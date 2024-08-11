FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запускаем команду для Django-приложения
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]