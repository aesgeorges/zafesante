from django.urls import path

from . import views

urlpatterns = [
    path('', views.questions_list, name='questions'),
    path('<slug:slug>/', views.single_question, name='single_question'),
    path('<slug:slug>/vote', views.vote, name='vote'),
]
