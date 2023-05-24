from django.http import HttpResponse


def projects_list(request):
    """Отображение всех проектов"""
    return HttpResponse("Hello, world. Здесь будут находиться все проекты")


def project_detail(request, project_id):
    """Отображение подробной информации о проекте"""
    response = "Подробная информация о проекте "
    return HttpResponse(response + str(project_id))
