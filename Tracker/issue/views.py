from django.http import HttpResponse


def issues_list(request, project_id):
    """Отображение всех задач"""
    return HttpResponse(f"Все задачи проекта {project_id}")


def issue_detail(request, project_id, issue_id):
    """Отображение подробной информации о проекте"""
    return HttpResponse(f"Задача {issue_id} из проекта {project_id}")
