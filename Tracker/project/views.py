from django.http import HttpResponse


def index(request):
    """Отображение всех проектов"""
    return HttpResponse("Hello, world. Это индекс проекта")


def detail(request, project_id):
    """Отображение подробной информации о проекте"""
    response = "Проект %s"
    return HttpResponse(response % project_id)