# Generated by Django 5.1.6 on 2025-03-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[("Habitaciones", "Habitaciones")], max_length=20, null=True
            ),
        ),
    ]
