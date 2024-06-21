# taskmanager/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
