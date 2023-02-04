from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('users', views.users, name = 'users'),
    path('cursos', views.cursos, name = 'cursos'),

]
