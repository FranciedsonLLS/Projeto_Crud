"""Projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app.models import models
from django.urls import path
from app.views import Lista_Clientes, Create_Clientes, Update_Clientes, Delete_Clientes, home
from app.views import Lista_Filmes , Create_Filmes , Update_Filmes, Delete_Filmes
from app.views import Lista_Reservas , Create_Reservas , Update_Reservas, Delete_Reservas
urlpatterns = [   
    #HOME PAGE
    path('admin/', admin.site.urls),
    path('', home),

    # CRUD URL DE CLIENTES #
    path('Clientes/', Lista_Clientes, name='url_clientes'),
    path('Criar_Cliente/', Create_Clientes, name='url_create_cliente'),
    path('Editar_Cliente/<int:pk>/', Update_Clientes, name="url_update_cliente"),
    path('Delete_Cliente/<int:pk>/', Delete_Clientes, name="url_delete_cliente"),

    #CRUD URL DE FILMES #
    path('Filmes/', Lista_Filmes, name='url_filmes'),
    path('Criar_Filme/', Create_Filmes, name='url_create_filme'),
    path('Editar_Filmes/<int:pk>/', Update_Filmes, name='url_update_filme'),
    path('Delete_Filmes/<int:pk>/', Delete_Filmes, name='url_delete_filme'),

    # CRUD URL DE RESERVAS #
    path('Reservas/', Lista_Reservas, name='url_reservas'),
    path('Criar_Reserva/', Create_Reservas, name='url_create_reservas'),
    path('Editar_Reservas/<int:pk>/', Update_Reservas, name='url_update_reservas'),
    path('Delete_Reservas/<int:pk>/', Delete_Reservas, name='url_delete_reservas'),
]
