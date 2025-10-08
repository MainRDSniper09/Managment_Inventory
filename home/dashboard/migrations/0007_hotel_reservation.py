# Generated manually due to limited execution environment
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                (
                    'amenities',
                    models.CharField(
                        blank=True,
                        help_text='Servicios destacados separados por coma (Wi-Fi, Piscina, etc.)',
                        max_length=255,
                    ),
                ),
                ('nightly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    'rating',
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text='Calificación promedio del hotel (0-5).',
                        max_digits=3,
                        null=True,
                    ),
                ),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotels/')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hoteles',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guests', models.PositiveIntegerField(default=1)),
                ('special_requests', models.TextField(blank=True)),
                (
                    'status',
                    models.CharField(
                        choices=[('pending', 'Pendiente'), ('confirmed', 'Confirmada'), ('cancelled', 'Cancelada')],
                        default='pending',
                        max_length=20,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'hotel',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reservations',
                        to='dashboard.hotel',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reservations',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Reservación',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
    ]
