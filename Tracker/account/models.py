from django.db import models
from django.conf import settings


class Division(models.Model):
    """Модель подразделения"""
    name = models.CharField(max_length=100, null=False, unique=True, verbose_name='Название')
    parent_division = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Родительское подразделение')

    def __str__(self):
        """Строковое представление объекта"""
        return self.name


class Position(models.Model):
    """Модель должности сотрудника"""
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        """Строковое представление объекта"""
        return self.name


class Profile(models.Model):
    """Расширенная модель пользователя для хранения требуемой информации"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Строковое представление пользователя"""
        return f'Профиль пользователя {self.user.username}'

    def get_absolute_url(self):
        pass