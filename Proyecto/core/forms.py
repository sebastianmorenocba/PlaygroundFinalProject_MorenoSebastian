from django import forms

from . import models


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = models.Mecanico
        fields = "__all__"

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = "__all__"

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
