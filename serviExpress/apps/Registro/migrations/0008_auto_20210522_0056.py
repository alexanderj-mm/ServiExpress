# Generated by Django 3.1.8 on 2021-05-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_cliente_fecha_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido_m',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellido_p',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='fono',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='vigente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_usuario',
            field=models.IntegerField(default=0),
        ),
    ]
