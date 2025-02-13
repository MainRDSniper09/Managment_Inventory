from django import forms
from .models import Cuadrilla, AsignacionCuadrilla

class CuadrillaForm(forms.ModelForm):
    class Meta:
        model = Cuadrilla
        fields = ['nombre', 'ubicacion']

class AsignacionCuadrillaForm(forms.ModelForm):
    class Meta:
        model = AsignacionCuadrilla
        fields = ['instalacion', 'cuadrilla', 'miembros_asignados']