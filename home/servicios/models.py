from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_estimado_instalacion = models.DurationField()

    def __str__(self):
        return self.nombre

class InstalacionServicio(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    servicio = models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_instalacion = models.DateTimeField()
    estado = models.CharField(max_length=50)
    cuadrilla = models.ForeignKey('cuadrillas.Cuadrilla', on_delete=models.CASCADE)

    def __str__(self):
        return f"Instalación de {self.servicio.nombre} para {self.cliente.usuario.username}"

class DetalleInstalacionServicio(models.Model):
    instalacion_servicio = models.ForeignKey('servicios.InstalacionServicio', on_delete=models.CASCADE)
    insumo = models.ForeignKey('insumos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.insumo.nombre} para {self.instalacion.servicio.nombre}"