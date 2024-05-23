from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Department(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Role(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    phone = models.CharField(max_length=255 , verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    password1 = models.CharField(max_length=255,  verbose_name='Пароль')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Status(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = 'Статус'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.description[:50]}"

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = 'Заявки'