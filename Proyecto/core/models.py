from django.db import models


class Mecanico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    dominio = models.CharField(max_length=50)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.marca} ({self.modelo}) - {self.mecanico}"


class VehiculoCliente(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.vehiculo} {self.cliente}"

class Servicio(models.Model):
    NOMBRE_CHOICES = [
        ('Cambio de aceite', 'Cambio de aceite'),
        ('Reemplazo de frenos', 'Reemplazo de frenos'),
        ('Alineación y balanceo', 'Alineación y balanceo'),
        ('Reparación de motor', 'Reparación de motor'),
        # Se pueden agregar más en esta sección 
    ]

    nombre = models.CharField(max_length=50, choices=NOMBRE_CHOICES)
    descripcion = models.TextField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    fecha_servicio = models.DateField()
    costo_reparacion = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.fecha_servicio}"