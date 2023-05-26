from django.db import models
from django.conf import settings


class Division(models.Model):
    """Модель подразделения"""
    name = models.CharField(max_length=100, null=False)


class Position(models.Model):
    """Модель должности сотрудника"""
    name = models.CharField(max_length=100, null=False)


class Profile(models.Model):
    """Расширенная модель пользователя для хранения требуемой информации"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    div_id = models.ForeignKey(Division, on_delete=models.SET_NULL)

    def __str__(self):
        """Строковое представление пользователя"""
        return f'Profile for user {self.user.username}'
