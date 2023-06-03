from django.urls import path, include
from . import views


urlpatterns = [
    path("<int:user_id>/", views.profile_detail, name="profile_detail"),]
