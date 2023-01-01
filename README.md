# О проекте  
API Yatabe позволяет делать запросы к русурсам **posts**, **comments**, **groups**, **follows**.  
Ресурсы **posts** и  **comments** отвечают за создание, редактирование и просмотр постов а также комментариев к ним.  
Ресурс **groups** служит для просмотра групп,к которым относятся посты.  
Ресурс **follows** отвечает за возможность подписки на пользователей.  
Просмотр ресурсов доступен всем, создание и изменение доступно авторизованным пользователям.  
Авторизация происходит с помощью joser.  
## Примеры запросов  
Get запрос к ресурсу posts.  
Ответ:  
```
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
## Установка  

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Asterrus/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

