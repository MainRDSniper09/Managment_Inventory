from django import forms
from .models import Producto, Bodega

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'stock_minimo', 'bodega']

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'direccion', 'ciudad', 'estado', 'codigo_postal']