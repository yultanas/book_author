# Book_Author

![Build Status](https://github.com/yultanas/book_author/actions/workflows/ci.yml/badge.svg)

## Обзор проекта

Это API-проект на основе Django для управления авторами и книгами. В проекте используется Tastypie для создания API, SQLite3 в качестве базы данных и Docker для контейнеризации.

## Особенности

- **RESTful API**: Создано с использованием Tastypie.
- **Операции CRUD**: Поддерживаются для авторов и книг.
- **База данных**: Используется SQLite3.
- **Docker**: Приложение упаковано в Docker для удобства развертывания.

## Требования

- Docker
- Docker Compose
- Python 3.11
- pip

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yultanas/book_author.git
    cd book_author
    ```
2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```
3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Настройте секреты:

    Создайте файл `secrets.py` в папке `base` и добавьте в него секретный ключ:

    ```python
    SECRET_KEY = 'django-insecure-n6h&!l*5o&99)^@w)v66%y9p3vq#t!a5#5y5f&g*yza2ht22#e'
    ```

## Запуск

### Локальный запуск (без Docker)

1. Примените миграции базы данных:

    ```bash
    python manage.py migrate
    ```

2. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

### Запуск с Docker

1. Соберите и запустите контейнеры:

    ```bash
    docker-compose up --build
    ```

2. Приложение будет доступно по адресу: [http://127.0.0.1:8000](http://http://127.0.0.1:8000).

## Тестирование

Для запуска тестов используйте следующую команду:
    
    ```bash
    python manage.py test
    ```
## API
API предоставляется через Tastypie и поддерживает следующие эндпоинты:

/api/v1/authors/ — CRUD для авторов.
/api/v1/books/ — CRUD для книг.    

## CI/CD
Проект использует GitHub Actions для автоматического запуска тестов при каждом пуше в ветку main. Статус билда отображается вверху этого README.