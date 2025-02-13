from django.db import models

# Create your models here.

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega_estimada = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=100)
    bodega = models.ForeignKey('productos.Bodegas', on_delete=models.CASCADE)
    repartidor = models.ForeignKey('usuarios.Repartidores', on_delete=models.CASCADE)
    cliente = models.ForeignKey('usuarios.Clientes',on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.pk} para {self.cliente.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey('Pedidos', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} para Pedido {self.pedido.pk}"