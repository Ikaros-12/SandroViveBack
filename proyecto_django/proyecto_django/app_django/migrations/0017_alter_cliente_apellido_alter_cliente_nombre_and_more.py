# Generated by Django 5.0.4 on 2024-09-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0016_remove_pedido_producto_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]