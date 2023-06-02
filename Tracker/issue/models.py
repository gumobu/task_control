from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Issue(models.Model):
    """Модель задачи с основными полями"""
    statuses = [
        ('CRT', 'Создана'),
        ('ANA', 'В анализе'),
        ('WRK', 'В работе'),
        ('DCL', 'Отменена'),
        ('END', 'Завершена'),
    ]
    id = models.AutoField(primary_key=True, verbose_name='issue')  # Идентификатор задачи
    project = models.ForeignKey('project.Project', related_name='issues', null=True, on_delete=models.SET_NULL)  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')  # Название задачи
    description = models.TextField(null=True, verbose_name='Описание')  # Описание задачи
    status = models.CharField(max_length=3, choices=statuses, default='CRT')
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата создания')  # Дата создания задачи
    updated_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата обновления')  # Дата обновления задачи
    plan_end_date = models.DateField(null=False, default=timezone.now().date() + timezone.timedelta(7), verbose_name="Плановая дата завершения")
    fact_end_date = models.DateTimeField(null=True, verbose_name='Фактическая дата завершения задачи')  # Дата завершения задачи
    parent_issue = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child')  # Идентификатор родительской задачи
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
        return str(self.id)

    @property
    def is_over_due(self):
        return timezone.now().date() > self.plan_end_date

    def get_absolute_url(self):
        return reverse('issue', kwargs={'issue_id':self.id})
