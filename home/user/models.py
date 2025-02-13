from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO Arreglar el porque no funciona la imagen 
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=20, null=True)
    imagen = models.ImageField(default='avatar.jpg', upload_to='Profile_Imagenes')

    def __str__(self):
        return f'{self.staff.username}-Perfil'

