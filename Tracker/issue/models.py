from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Issue(models.Model):
    """Модель задачи с основными полями"""
    id = models.AutoField(primary_key=True, verbose_name='Задача')  # Идентификатор задачи
    project = models.ForeignKey('project.Project', null=True, on_delete=models.SET_NULL)  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')  # Название задачи
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата создания')  # Дата создания задачи
    updated_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата обновления')  # Дата обновления задачи
    end_date = models.DateTimeField(null=True, verbose_name='Дата закрытия')  # Дата завершения задачи
    parent_issue = models.ForeignKey('self', on_delete=models.CASCADE, null=True)  # Идентификатор родительской задачи
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')  # Автор задачи
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assignee')  # Исполнитель задачи
    watcher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='watcher')  # Наблюдатель задачи

    def end(self):
        """Метод для завершения задачи"""
        self.end_date = timezone.now()
        self.save()

    def create(self):
        """Метод для создания задачи"""
        pass

    def update(self):
        """Метод обновления задачи"""
        pass

    def __str__(self):
        """Строковое представление задачи - ее идентификатор"""
        return self.id
