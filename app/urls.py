from django.contrib import admin
from django.urls import path

from . import views

# Application URLs

urlpatterns = [
    path('', views.index),
]
