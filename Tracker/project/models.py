from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    """Модель проекта с основными полями"""
    id = models.CharField(max_length=15, unique=True, primary_key=True)  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True)  # Название проекта
    created_date = models.DateTimeField(auto_now_add=True)  # Дата создания проекта
    start_date = models.DateTimeField(auto_now_add=True)  # Дата начала проекта
    end_date = models.DateTimeField(blank=True, null=True)  # Дата окончания проекта

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
