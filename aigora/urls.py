from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.signup,name='signup'),
    path('display',views.display,name='display'),
    path('profile', views.profile, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()
