# Generated by Django 3.1.8 on 2021-05-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0005_reservahora_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fono',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='cliente',
            name='mail',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vehiculo_marca',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vehiculo_modelo',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vehiculo_patente',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vigente',
            field=models.CharField(default='', max_length=2),
        ),
    ]
