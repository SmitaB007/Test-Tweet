"""
URL configuration for tweetSystem project.

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
from . import views

urlpatterns = [
     path('', views.list_tweets ,name='list_tweets'),
     path('register/', views.register,name='register'),
     path('logout/', views.logout_user,name='logout_user'),
     path('create/', views.create_tweet,name='create_tweet'),
     path('<int:tweet_id>/edit/', views.edit_tweet,name='edit_tweet'),
     path('<int:tweet_id>/delete/', views.delete_tweet,name='delete_tweet'),
     path('search/', views.search_user,name='search_user'),

     
] 


