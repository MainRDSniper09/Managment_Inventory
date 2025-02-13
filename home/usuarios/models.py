
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
     TIPO_USUARIO_CHOICES =[
         ('cliente', 'Cliente'),
         ('administrativo', 'Administrativo'),
         ('administrador', 'Administrador'),
         ('repartidor', 'Repartidor'),
         ('cuadrilla', 'Cuadrilla'),
     ]
     tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

class Cliente(models.Model):
     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
     direccion = models.CharField(max_length=255)
     ciudad = models.CharField(max_length=20)
     codigo_postal = models.CharField(max_length=20)

class Repartidor(models.Model):
     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
     disponibilidad = models.BooleanField(default=True)
     #bodega = models.ForeignKey('productos.Bodega', on_delete=models.CASCADE)

class MiembroCuadrilla(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    #cuadrilla = models.ForeignKey('cuadrillas.Cuadrilla', on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)

class Administrativo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=50)