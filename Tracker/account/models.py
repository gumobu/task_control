from django.db import models
from django.conf import settings


class Division(models.Model):
    """Модель подразделения"""
    name = models.CharField(max_length=100, null=False, unique=True)
    parent_division = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)


class Position(models.Model):
    """Модель должности сотрудника"""
    name = models.CharField(max_length=100, null=False, unique=True)


class Profile(models.Model):
    """Расширенная модель пользователя для хранения требуемой информации"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Строковое представление пользователя"""
        return f'Profile for user {self.user.username}'
