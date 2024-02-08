from django.contrib import admin

from . import models

admin.site.register(models.Vehiculo)
admin.site.register(models.VehiculoCliente)
admin.site.register(models.Cliente)
admin.site.register(models.Mecanico)
