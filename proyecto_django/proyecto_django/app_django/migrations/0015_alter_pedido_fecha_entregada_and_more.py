# Generated by Django 5.0.4 on 2024-09-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0014_alter_producto_talle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_entregada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pactada',
            field=models.DateField(blank=True, null=True),
        ),
    ]