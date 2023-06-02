from django.shortcuts import render
from .models import *


def projects_list(request):
    """Отображение всех проектов"""
    title = "Список существующих проектов"
    projects = Project.objects.all()
    page_title = 'Список проектов'
    return render(request, 'project/projects_list.html', locals())


def project_detail(request, project_id):
    """Отображение подробной информации о проекте"""
    page_title = f'Проект {project_id}'
    title = page_title
    project = Project.objects.get(id=project_id)
    cur_date = timezone.now().date()
    issues = project.issues.all()
    return render(request, 'project/project_detail.html', locals())


def create_project(request, **kwargs):
    """Добавление проекта в базу"""
    pass
