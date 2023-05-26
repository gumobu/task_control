from django.http import HttpResponse


def profile_detail(request, user_id):
    """Отображение информации о аккаунте"""
    return HttpResponse(f"Информация о аккаунте {user_id}")
