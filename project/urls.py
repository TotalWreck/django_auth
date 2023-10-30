from django.contrib import admin
from django.urls import path, include

# Project URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]