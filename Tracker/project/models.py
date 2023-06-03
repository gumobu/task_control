from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Project(models.Model):
    """Модель проекта с основными полями"""
    id = models.AutoField(unique=True, primary_key=True, verbose_name='Проект')  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')  # Название проекта

    def __str__(self):
        """Строковое представление проекта"""
        return f'[{self.id}] {self.title}'

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_id': self.id})

    def clean_plan_end_date(self):
        """Проверка на корректность введенной плановой даты окончания проекта"""
        date = self.cleaned_data['plan_end_date']
        if date <= timezone.now().date():
            """Если дата меньше текущей даты"""
            raise ValidationError('Плановая дата окончания установлена не больше текущей')
        return date

    @property
    def get_issues_count(self):
        return self.issues.all().count()
