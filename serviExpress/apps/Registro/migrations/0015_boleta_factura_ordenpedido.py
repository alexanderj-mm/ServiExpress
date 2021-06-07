# Generated by Django 3.1.8 on 2021-06-07 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0014_auto_20210605_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordenPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('descripcion_pedido', models.TextField()),
                ('cantidad_prod_pedido', models.IntegerField()),
                ('precio_prod_unidad', models.IntegerField()),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factura', models.DateField()),
                ('cantidad_factura', models.IntegerField()),
                ('subtotal_factura', models.IntegerField()),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.cliente')),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_boleta', models.DateField()),
                ('cantidad_boleta', models.IntegerField()),
                ('subtotal_boleta', models.IntegerField()),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.cliente')),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
