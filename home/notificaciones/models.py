from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Notificacion(models.Model):
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f"Notificación para {self.usuario.username}"