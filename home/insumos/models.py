from django.db import models

# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    bodega = models.ForeignKey('productos.Bodega', on_delete=models.CASCADE)

class ChecklistInsumo(models.Model):
    instalacion = models.ForeignKey('servicios.InstalacionServicio', on_delete=models.CASCADE)
    insumo = models.ForeignKey('insumos.Insumo', on_delete=models.CASCADE)
    cantidad_requerida = models.IntegerField()
    cantidad_verificada = models.IntegerField()
    verificado = models.BooleanField(default=False)
    miembro_cuadrilla = models.ForeignKey('cuadrillas.MiembroCuadrilla', on_delete=models.CASCADE)
