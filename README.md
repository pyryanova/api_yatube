# API Yatube

REST API для социальной сети Yatube. Пользователи могут публиковать посты, комментировать их, подписываться на авторов. Реализована аутентификация по токену, разграничение прав доступа и сериализация данных.

## Технологии

- Python 3.8+
- Django 3.2
- Django REST Framework
- TokenAuthentication
- SQLite (по умолчанию)
- Pytest

## Начало работы

1. Клонируйте репозиторий:

```bash
git clone https://github.com/pyryanova/api_yatube.git
cd api_yatube
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции:

```bash
python yatube_api/manage.py migrate
```

5. Запустите сервер разработки:

```bash
python yatube_api/manage.py runserver
```

## Аутентификация

Используется `TokenAuthentication`.

- Получение токена:
  ```http
  POST /api/v1/api-token-auth/
  ```

- Пример запроса:
  ```json
  {
    "username": "ваш_логин",
    "password": "ваш_пароль"
  }
  ```

- Токен передаётся в заголовке:
  ```
  Authorization: Token <ваш_токен>
  ```

## Тестирование

```bash
pytest
```

## Postman

Для ручного тестирования можно использовать коллекцию запросов:

```bash
cd postman_collection
bash set_up_data.sh
```

Файл `CRUD_for_yatube.postman_collection.json` можно импортировать в Postman для тестирования API.

## Структура проекта

- `yatube_api/` — основной код Django-проекта и приложений
- `api/` — реализация API: сериализаторы, вьюсеты, маршруты
- `posts/` — модели и бизнес-логика
- `tests/` — автоматические тесты

## Лицензия

Проект создан в учебных целях.
