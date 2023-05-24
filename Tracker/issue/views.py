from django.http import HttpResponse


def issues_list(request, project_id):
    """Отображение всех задач"""
    return HttpResponse(f"Hello, world. Здесь будут находиться все задачи проекта {project_id}")


def issue_detail(request, issue_id):
    """Отображение подробной информации о проекте"""
    return HttpResponse(f"Информация о задаче {issue_id}")
