from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path



urlpatterns = [
    path("", views.index, name="index"),
    path("profesor/list", views.profesor_list, name="profesor_list"),
    path("profesor/create", views.profesor_create, name="profesor_create"),
    path("estudiante/list", views.estudiante_list, name="estudiante_list"),
    path("estudiante/create", views.estudiante_create, name="estudiante_create"),
    path("curso/list", views.curso_list, name="curso_list"),
    path("curso/create", views.curso_create, name="curso_create"),
    path('admin/', admin.site.urls)
]
