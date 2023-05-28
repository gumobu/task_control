from django.shortcuts import render
from .models import *


def projects_list(request):
    """Отображение всех проектов"""
    projects = Project.objects.all()
    page_title = 'Список проектов'
    return render(request, 'project/projects_list.html', locals())


def project_detail(request, project_id):
    """Отображение подробной информации о проекте"""
    page_title = f'Проект {project_id}'
    project = Project.objects.get(id=project_id)
    return render(request, 'project/project_detail.html', locals())
