"""
URL configuration for moviehub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home, name="Home"),
    path('' , views.home, name="Home"),
    path('index/' , views.home, name="Home"),
    path('video_view/<int:video_id>/', views.videoView, name="video_view"),
    path('nav/', views.nav, name="nav"),
    path('movies/', views.movies, name="movies"),
    path('webseries/', views.webseries, name="webseries"),
    path('hollywood/', views.hollywood, name="hollywood"),
    path('bollywood/', views.bollywood, name="bollywood"),
    path('search',views.search,name='search'),
]
