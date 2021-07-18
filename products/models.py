from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class product(models.Model):
    name = models.CharField(verbose_name='Имя', db_index=True, unique=True, max_length=64)
    price = models.CharField(verbose_name='Цена', max_length=64)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
