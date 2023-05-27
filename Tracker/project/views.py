from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def projects_list(request):
    """Отображение всех проектов"""
    projects = Project.objects.all()
    return render(request, 'projects_list.html', locals())


def project_detail(request, project_id):
    """Отображение подробной информации о проекте"""
    response = "Подробная информация о проекте "
    return HttpResponse(response + str(project_id))
