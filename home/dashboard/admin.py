from django.contrib import admin
from .models import Product,Order # Importamos el modelo Product y Order
from django.contrib.auth.models import Group # Importamos el modelo Group

admin.site.site_header = "Administracion" # Cambiamos el nombre del panel administrativo

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity') # Indicamos los campos que queremos mostrar en el panel administrativo
    list_filter = ['category',] # Indicamos los campos que queremos filtrar en el panel administrativo

# Register your models here.

admin.site.register(Product, ProductAdmin) # Registramos el modelo Product en nuestro panel administrativo
admin.site.register(Order) # Registramos el modelo Order en nuestro panel administrativo

# admin.site.unregister(Group) # Desregistramos el modelo Group en nuestro panel administrativo
