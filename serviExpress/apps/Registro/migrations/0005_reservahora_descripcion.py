# Generated by Django 3.1.8 on 2021-05-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservahora',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
    ]
