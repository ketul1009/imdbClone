import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('genre', views.genre, name='genre'),
    path('movies', views.movies, name='movies'),
    path('movies/<int:id>', views.update, name="update")
]