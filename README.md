# Django Tree Menu
Реализация древовидного меню на Django

### Начало работы

1. Склонируйте проект:

```git clone https://github.com/hlystovea/django-tree-menu.git```  

2. Создайте файл .env по примеру env.example.
 

3. Запустите контейнеры:

```docker-compose up -d```

4. Запустите миграции:

```docker-compose exec backend python manage.py migrate --noinput```

5. Соберите статику:

```docker-compose exec backend python manage.py collectstatic --no-input```

6. Создайте своего суперпользователя:

```docker-compose exec backend python manage.py createsuperuser```

7. Сайт будет доступен по адресу:
 
```http://127.0.0.1:8003```
