from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.issues_list, name="issues_list"),
    path("<int:issue_id>/", views.issue_detail, name="issue"),
    path('create/', views.create_issue, name='create_issue'),
    path('update/<int:issue_id>/', views.update_issue, name='update_issue'),
]
