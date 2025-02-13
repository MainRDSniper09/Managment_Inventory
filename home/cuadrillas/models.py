from django.db import models
from usuarios.models import MiembroCuadrilla
from servicios.models import InstalacionServicio

# Create your models here.

class Cuadrilla(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class AsignacionCuadrilla(models.Model):
    instalacion = models.ForeignKey('servicios.InstalacionServicio', on_delete=models.CASCADE)
    cuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    miembros_asignados = models.ManyToManyField('usuarios.MiembroCuadrilla')

    def __str__(self):
        return f"Asignación de {self.cuadrilla.nombre} a {self.instalacion.id}"