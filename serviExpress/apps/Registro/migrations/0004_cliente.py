# Generated by Django 3.1.8 on 2021-05-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_auto_20210512_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
            ],
        ),
    ]
