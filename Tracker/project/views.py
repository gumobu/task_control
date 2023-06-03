from django.shortcuts import render
from .models import *
from .forms import AddProject


def projects_list(request):
    """Отображение всех проектов"""
    title = "Список существующих проектов"
    projects = Project.objects.all()
    page_title = 'Список проектов'
    return render(request, 'project/projects_list.html', locals())


def project_detail(request, project_id):
    """Отображение подробной информации о проекте"""
    project = Project.objects.get(id=project_id)
    page_title = f'[{project_id}] {project.title}'
    title = page_title
    cur_date = timezone.now().date()
    issues = project.issues.all()
    return render(request, 'project/project_detail.html', locals())


def create_project(request):
    if request.method == 'POST':
        form = AddProject(request.POST)
        if form.is_valid():
            project = form.save()
    else:
        form = AddProject()
    return render(request, 'project/create_project.html', locals())
