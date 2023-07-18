# API NetConnect

Данный репозиторий включает в себя REST-API для платформы NetConnect.


## Зависимости

Для работоспобности необходимые следующие библиотеки:
>Python 3.10
Django 3.2.16  
pytest 6.2.4  
pytest-pythonpath 0.7.3  
pytest-django 4.4.0  
djangorestframework 3.12.4  
djangorestframework-simplejwt 4.7.2  
Pillow 9.3.0  
PyJWT 2.1.0  
requests 2.26.0

## Установка

Клонируйте репозиторий коммандой `git clone git@github.com:mxstrv/api_netconnect.git`

Создайте виртуальное окружение   `python3 -m venv venv`

Активируйте виртуальное окружение `source venv/bin/activate`

Установите зависимости `pip install -r requirements.txt`

Запустите сервер `python manage.py runserver`
 
## Что поддерживается

Интегрирована поддержка JWT Token с использованием библиотек djoser и PyJWT

|              |Метод запроса                        |
|------------------------------------------|-----------------------------|
Неавторизованный пользователь     |`GET, HEAD, OPTIONS`               
Зарегистрированный пользователь   |`GET, PUT, PATCH, DELETE, HEAD, OPTIONS`            


## Как пользоваться
Удобнее всего отправлять запросы с использованием [Postman](https://www.postman.com/). Ниже приведены примеры запросов и ответов:

Регистрируемся по адресу `http://127.0.0.1:8000/api/v1/users/` POST запросом:
```
{
"username":  "username",
"password":  "password"
}
```
 Получаем токен `http://127.0.0.1:8000/api/v1/jwt/create/`:
```
{
"refresh":  "...",
"access":  "..."
}
```
Данные из access вставляем в **Postman** в формате `Bearer access`

## Примеры запросов

### Получение списка постов и создание поста, а также их удаление
`http://127.0.0.1:8000/api/v1/posts/` (поддерживается поиск и пагинация при наличии limit offset параметров)

Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Пример PUT запроса:

### Получение списка комментариев поста и написание их
`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`

Пример ответа:
```
[
{
"id":  1,
"author":  "user1",
"text":  "text",
"created":  "2023-02-21T11:41:59.915346Z",
"post":  1
},
{
"id":  2,
"author":  "user2",
"text":  "text",
"created":  "2023-02-21T11:47:39.836172Z",
"post":  1
}
]
```

### Работа с группами
`http://127.0.0.1:8000/api/v1/groups/`

Пример ответа:
```
[
{
"id":  1,
"title":  "TEST",
"slug":  "test",
"description":  "test group 1"
},
{
"id":  2,
"title":  "TEST2",
"slug":  "test2",
"description":  "test group 2"
}
]
```
### Модель подписок на пользователей
`http://127.0.0.1:8000/api/v1/follow/` (поддерживается поиск по подпискам)

Пример ответа:
```
[
{
"user":  "user",
"following":  "user2"
},
{
"user":  "user",
"following":  "user3"
}
]
```
## Документация OpenAPI
Подробная документация по проекту c использованием спецификации OpenAPI доступна по адресу `http://127.0.0.1:8000/redoc/`
