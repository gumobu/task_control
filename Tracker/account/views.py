from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


def profile_detail(request, user_id):
    title = f'Профиль {user_id}'
    page_title = 'Профиль'
    profile = Profile.objects.get(user=user_id)
    """Отображение информации о аккаунте"""
    return render(request, 'account/account_detail.html', locals())
