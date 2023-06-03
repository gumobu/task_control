from django.urls import path, include
from . import views


urlpatterns = [
    path("<str:user_id>/", views.profile_detail, name="profile_detail"),
]
