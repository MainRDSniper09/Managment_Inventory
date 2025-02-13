from django import forms
from .models import Insumo, ChecklistInsumo

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'stock', 'bodega']

class ChecklistInsumoForm(forms.ModelForm):
    class Meta:
        model = ChecklistInsumo
        fields = ['insumo', 'cantidad_requerida', 'cantidad_verificada', 'verificado']