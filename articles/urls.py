from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles_blog, name='blog'),
    path('<slug:slug>/', views.single_article, name='single_article'),
]
