# API Yatube

REST API для социальной сети **Yatube**.

Пользователи могут:
- публиковать посты;
- просматривать и комментировать чужие посты;
- подписываться на авторов (в рамках расширения проекта).

Реализована:
- аутентификация по токену (`TokenAuthentication`);
- разграничение прав доступа;
- вложенные ресурсы;
- сериализация и валидация данных через Django REST Framework.

---

## Технологии

- Python 3.8+
- Django 3.2
- Django REST Framework
- SQLite (по умолчанию)
- TokenAuthentication
- Pytest

---

## Установка и запуск

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/pyryanova/api_yatube.git
   cd api_yatube
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Windows: venv\Scripts\activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполнить миграции:

   ```bash
   python yatube_api/manage.py migrate
   ```

5. Запустить сервер разработки:

   ```bash
   python yatube_api/manage.py runserver
   ```

---

## Аутентификация

Используется `TokenAuthentication`.

- Получение токена:

  ```http
  POST /api/v1/api-token-auth/
  ```

- Пример тела запроса:

  ```json
  {
    "username": "ваш_логин",
    "password": "ваш_пароль"
  }
  ```

- Передача токена в заголовке:

  ```http
  Authorization: Token <ваш_токен>
  ```

> ⚠️ **Важно:** Все запросы к API доступны **только после авторизации**. Анонимные пользователи получают `401 Unauthorized`.

---

## Тестирование

Для запуска автотестов:

```bash
pytest
```

---

## Postman

Для ручной проверки API:

1. Перейдите в папку с коллекцией и выполните скрипт:

   ```bash
   cd postman_collection
   bash set_up_data.sh
   ```

   > ⚠️ Скрипт очистит текущую базу данных и создаст тестовые объекты.

2. Импортируйте файл `CRUD_for_yatube.postman_collection.json` в Postman.

3. Используйте коллекцию для отправки последовательных запросов к API.

---

## Лицензия

Проект создан в учебных целях в рамках обучения на Яндекс.Практикуме.
