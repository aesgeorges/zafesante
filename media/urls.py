from django.urls import path

from . import views

urlpatterns = [
    path('', views.videos_list, name='video_list'),
    path('<slug:slug>/', views.video, name='video'),
]
