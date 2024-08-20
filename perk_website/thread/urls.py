from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


from django.urls import path

urlpatterns = [
    path('', views.home, name='thread-home'),
    # path('', views.home, name='thread-home'),
    path('about/',views.about, name='thread-about'),
    path('league/',views.league, name='thread-league'),
    path('store/',views.store, name='thread-store'),
    path('thread/', PostListView.as_view(), name='thread-thread'),
    # path('thread/',views.thread, name='thread-thread'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('contact/',views.contact, name='thread-contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)