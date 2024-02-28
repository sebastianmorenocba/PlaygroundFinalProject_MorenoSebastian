from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

# LOGIN LOGOUT Y REGISTER
from .views import *



urlpatterns = [
    path("", views.index, name="index"),
    path("mecanico/list", views.mecanico_list, name="mecanico_list"),
    path("mecanico/create", views.mecanico_create, name="mecanico_create"),
    path("cliente/list", views.cliente_list, name="cliente_list"),
    path("cliente/create", views.cliente_create, name="cliente_create"),
    path("vehiculo/list", views.vehiculo_list, name="vehiculo_list"),
    path("vehiculo/create", views.vehiculo_create, name="vehiculo_create"),
    path("servicio/list", views.servicio_list, name="servicio_list"),
    path("servicio/create", views.servicio_create, name="servicio_create"),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('index/', index, name='index'),
    path('about/', views.about, name='about'),
]
