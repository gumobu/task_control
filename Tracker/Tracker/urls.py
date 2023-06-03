from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
    path('project/', include('project.urls')),
    path('issue/', include('issue.urls')),
    path("account/", include('account.urls')),
    path('analytics/', include('analytics.urls'))
]
