from django.db import models
from django.contrib.auth.models import User # Importamos el modelo User

# Base de datos de productos

# Create your models here.

CATEGORY = (
    ('Comp Electricos', 'Comp Electricos'),
    ('Computadores', 'Computadores'),
    ('Televisores', 'Televisores'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta: # Indicamos el nombre de la tabla
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}-{self.quantity}' # Retornamos el nombre del producto y la cantidad
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta: # Indicamos el nombre de la tabla
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}' # Retornamos el producto y el usuario que lo ordeno