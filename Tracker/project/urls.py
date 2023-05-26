from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.projects_list, name="Список проектов"),
    path("project/<str:project_id>/", views.project_detail, name="Проект"),
    path("project/<str:project_id>/issues/", include('issue.urls')),
    path("account/<str:user_id>/", include('account.urls')),
]
