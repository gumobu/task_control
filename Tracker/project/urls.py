from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.projects_list, name='project_list'),
    path("<int:project_id>/", views.project_detail, name="project"),
    path("create/", views.create_project, name='create_project'),
]
