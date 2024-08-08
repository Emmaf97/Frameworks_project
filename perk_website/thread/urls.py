from django.contrib import admin
from django.urls import path, include
from .import views

from django.urls import path

urlpatterns = [
    path('', views.home, name='thread-home'),
    path('about/',views.about, name='thread-about'),
]