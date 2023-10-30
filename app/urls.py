from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

# Application URLs

urlpatterns = [
    path('', views.index),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register),
    path('auth/', views.auth),
]
