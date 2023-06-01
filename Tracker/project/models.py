from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Project(models.Model):
    """Модель проекта с основными полями"""
    id = models.AutoField(unique=True, primary_key=True, verbose_name='Проект')  # Идентификатор проекта
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')  # Название проекта
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата создания')  # Дата создания проекта
    updated_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата обновления')  # Дата обновления проекта
    plan_end_date = models.DateField(null=True, verbose_name='Плановая дата закрытия')  # Дата завершения проекта
    fact_end_date = models.DateField(null=True, verbose_name='Фактическая дата закрытия')  # Дата завершения проекта

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

