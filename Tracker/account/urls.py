from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.profile_detail, name="Информация о аккаунте"),
]
