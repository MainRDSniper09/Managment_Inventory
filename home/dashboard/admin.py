from django.contrib import admin
from .models import Product # Importamos el modelo Product

# Register your models here.

admin.site.register(Product) # Registramos el modelo Product en nuestro panel administrativo
