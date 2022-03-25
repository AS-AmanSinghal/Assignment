"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from Assignment import views
from account import viewset
from posts import viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'login', viewset.LoginViewSet, basename='login')
router.register(r'users', viewset.MyUserViewSet, basename='users')
router.register(r'logout', viewset.LogoutViewSet, basename='logout')
router.register(r'post', viewsets.PostViewSets, basename='post')
router.register(r'follow', viewset.FollowerViewSet, basename='follow')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('users/', include('account.urls')),
    path('', views.home, name='home'),
    path('users/', include('account.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
