from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    """Модель проекта с основными полями"""
    id = models.AutoField(unique=True, primary_key=True, verbose_name='Проект')  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')  # Название проекта
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата создания')  # Дата создания проекта
    updated_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата обновления')  # Дата обновления проектам
    end_date = models.DateTimeField(null=True, verbose_name='Дата закрытия')  # Дата завершения проекта

    def end(self):
        """Метод для завершения проекта"""
        self.end_date = timezone.now()
        self.save()

    def create(self):
        """Метод для создания проекта"""
        pass

    def update(self):
        """Метод обновления проекта"""
        pass

    def __str__(self):
        """Строковое представление проекта - его идентификатор"""
        return self.id
