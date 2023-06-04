from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.analytics_main, name="analytics_main"),
    path("by_projects/", views.by_projects, name="by_projects"),
    path("by_users/", views.by_users, name="by_users"),
]
