from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('project.urls')),
    path('issue/', include('issue.urls')),
    path("account/<str:user_id>/", include('account.urls')),
]
