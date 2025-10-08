from django.db import models
from django.contrib.auth.models import User # Importamos el modelo User


class Hotel(models.Model):
    """Modelo que representa los hoteles disponibles para reservar."""

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    amenities = models.CharField(
        max_length=255,
        blank=True,
        help_text="Servicios destacados separados por coma (Wi-Fi, Piscina, etc.)",
    )
    nightly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="Calificación promedio del hotel (0-5).",
    )
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        return self.name

# Base de datos de productos

# Create your models here.

CATEGORY = (
    ('Habitaciones', 'Habitaciones'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Agregar este campo

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

    
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


class Reservation(models.Model):
    """Reservas realizadas por los clientes para los distintos hoteles."""

    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pendiente'),
        (CONFIRMED, 'Confirmada'),
        (CANCELLED, 'Cancelada'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations')
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'

    def __str__(self):
        return f'Reserva de {self.user.username} en {self.hotel.name}'

    @property
    def nights(self):
        return (self.check_out - self.check_in).days