from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from . import models


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = models.Mecanico
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = models.Vehiculo
        fields = "__all__"

class CustomAuthenticationForm(AuthenticationForm):
    # Agrega cualquier campo adicional o personalización si es necesario
    class Meta:
        model = User  # Reemplaza con tu modelo de Usuario
        fields = ['username', 'password']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields = "__all__"
        widgets = {
            'fecha_servicio': forms.DateInput(attrs={'type': 'date'}),
            'costo_reparacion': forms.TextInput(attrs={'placeholder': '$'}),
        }
        
