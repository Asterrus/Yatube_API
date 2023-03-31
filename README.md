### Описание

   Проект Yatube API позволяет пользователям публиковать блоги.<br/>  
   Добавлять группы, к которым относятся блоги, может только администратор.<br/>
   Пользователи могут оставлять комментарии к блогам.<br/>
   Реализован функционал подписки пользователй друг на друга.<br/>
   Создавать посты, комментарии и подписываться могут только аутентифицированные пользователи.<br/>   
   Каждый ресурс описан в документации: указаны эндпоинты (адреса, по которым можно сделать запрос),    
разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.<br/>        
   

### Технологии:
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![DRF](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
### Используемые пакеты:
    *  Django==3.2.16
    *  pytest==6.2.4
    *  pytest-pythonpath==0.7.3
    *  pytest-django==4.4.0
    *  djangorestframework==3.12.4
    *  djangorestframework-simplejwt==4.7.2
    *  Pillow==9.3.0
    *  PyJWT==2.1.0
    *  requests==2.26.0
    *  djoser==2.1.0

### Установка

1. Клонировать репозиторий:

   ```python
   git clone ...
   ```

2. Перейти в папку с проектом:

   ```python
   cd Yatube_API/
   ```

3. Установить виртуальное окружение для проекта:

   ```python
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate
   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```python
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```python
   cd yatube_api/
   python3 manage.py migrate
   ```

7. Запустить проект:
   ```python
   python manage.py runserver
   ```
### Дополнительно

* Каждый ресурс описан в документации проекта:
   ```
   http://127.0.0.1:8000/redoc/
   ```

* ПО для тестирования API:
   ```
   https://www.postman.com/
   ```
### Примеры запросов  
* Получение JWT-токена в обмен на `username` и `password`. Доступно без токена.  
    `POST http://127.0.0.1:8000/api/v1/jwt/create/`
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
* Пример ответа:
    ```json
    {
        "refresh": "string",
        "access": "string"
    }
    ```
* Пример GET-запроса к ресурсу posts(Блоги).
   Получение списка всех блогов. Доступно без токена.
   `GET http://127.0.0.1:8000/api/v1/posts/`
* Пример ответа:
   ```json
    {
       "count": 1,
       "next": null,
       "previous": null,
       "results": [
           {
               "id": 1,
               "author": "TestUser",
               "text": "Образец поста",
               "pub_date": "2023-01-01T19:56:01.961065Z",
               "image": null,
               "group": null
           }
       ]
    }
   ```
* Пример POST-запроса к ресурсу posts(Блоги).
   Добавление нового блога. Необходим токен.  
   `GET http://127.0.0.1:8000/api/v1/posts/`
   ```json
    {
      "text": "string",
      "image": "string",
      "group": 0
    }
   ```
* Пример ответа:
   ```json
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
   ```

### Автор проекта 
* Роман Дячук   

