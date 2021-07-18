- python 3.9.0

- Используются библиотеки:
    - Django==2.1.7
    - djoser==1.6.0
    - djangorestframework==3.9.4
    (установка pip install "библиотека")

---
1. Переходим к папке:
```
    cd диск:/...
```

2. Запускаем сервер:
```
    .\manage.py runserver
```

3. Заходим на него:
```
    http://127.0.0.1:8000/
```

4. Чтобы добавлять товары, менять и удалять, нужно зарегистриртоваться:
```
    http://127.0.0.1:8000/api/v1/auth/
    Нужно будет нажать на create user.
```


5. Cоздание товара:
```
    http://127.0.0.1:8000/api/v1/products/product/create/
```

6. Просмотр всех товаров:
```
    http://127.0.0.1:8000/api/v1/products/all/
```

7. Редактирование товара:
```
    http://127.0.0.1:8000/api/v1/products/product/detail/ "id товара" /
```

---
Если не сохраняет товары:
```
    .\manage.py makemigrations
    .\manage.py migrate
```