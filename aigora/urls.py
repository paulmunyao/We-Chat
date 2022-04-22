from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup,name='registration/signup'),
    path('display',views.display,name='display'),
    path('profile', views.profile, name='profile'),
]
