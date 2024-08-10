from django.contrib import admin
from django.urls import path, include
from .import views

from django.urls import path

urlpatterns = [
    path('', views.home, name='thread-home'),
    path('about/',views.about, name='thread-about'),
    path('league/',views.league, name='thread-league'),
    path('store/',views.store, name='thread-store'),
    path('thread/',views.thread, name='thread-thread'),
    path('contact/',views.contact, name='thread-contact'),
]