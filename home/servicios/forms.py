# servicios/forms.py

from django import forms
from .models import Servicio, InstalacionServicio, DetalleInstalacionServicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'tiempo_estimado_instalacion']

class InstalacionServicioForm(forms.ModelForm):
    class Meta:
        model = InstalacionServicio
        fields = ['cliente', 'servicio', 'fecha_instalacion', 'estado', 'cuadrilla']

class DetalleInstalacionServicioForm(forms.ModelForm):
    class Meta:
        model = DetalleInstalacionServicio
        fields = ['instalacion', 'insumo', 'cantidad']
