from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.projects_list, name="project list"),
    path("<str:project_id>/", views.project_detail, name="project"),
    path("<str:project_id>/issue/", include('issue.urls')),
    #path("create_project/", views.create_project),
]
