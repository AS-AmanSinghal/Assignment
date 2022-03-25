from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]