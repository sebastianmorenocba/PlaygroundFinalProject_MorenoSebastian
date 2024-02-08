from django import forms

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
