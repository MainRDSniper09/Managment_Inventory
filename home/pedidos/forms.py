from django import forms
from .models import Pedidos, DetallePedido

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['cliente', 'fecha_entrega_estimada', 'estado', 'bodega', 'repartidor']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']
