"""
URL configuration for Proyecto_hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from .views import index,pagina2,InicioDeSesion,RegUsuario,Perfil,ListaUsuarios,RegReservas,Reservar,Catalogo,cerrarsesion

router = routers.DefaultRouter()
urlpatterns = [
    path('',InicioDeSesion,name='index'),
    path('nombreejemplo2',pagina2,name='nombreredireccionpagina2'),
    path('InicioDeSesion',InicioDeSesion,name='InicioDeSesion'),
    path('RegUsuario',RegUsuario,name='RegUsuario'),
    path('Perfil',Perfil,name='Perfil'),
    path('ListaUsuarios',ListaUsuarios,name='ListaUsuarios'),
    path('RegReservas',RegReservas,name='RegReservas'),
    path('Catalogo',Catalogo,name='Catalogo'),
    path('cerrarsesion/', cerrarsesion,name="cerrarsesion"),
    path('Reservar/<int:habitacion_id>/', Reservar,name="Reservar"), 
    #path('sub url',view, name="nombre")  
]
