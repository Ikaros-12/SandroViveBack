# Generated by Django 5.0.4 on 2024-06-24 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0011_alter_categoria_descripcion_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
