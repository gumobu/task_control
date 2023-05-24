from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.issues_list, name="Список задач"),
    path("<str:issue_id>/", views.issue_detail, name="Задача"),
]
