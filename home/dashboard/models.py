from django.db import models

# Base de datos de productos

# Create your models here.

CATEGORY = (
    ('Celulares', 'Celulares'),
    ('Computadores', 'Computadores'),
    ('Televisores', 'Televisores'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

