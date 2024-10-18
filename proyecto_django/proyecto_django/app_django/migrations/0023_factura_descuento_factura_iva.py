# Generated by Django 5.0.4 on 2024-10-18 03:06

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0022_estadopedido_alter_pedido_estado_delete_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12),
        ),
        migrations.AddField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12),
        ),
    ]