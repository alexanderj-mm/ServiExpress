from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cliente(models.Model): 
    id_usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo_marca=models.CharField(max_length=30)
    vehiculo_modelo=models.CharField(max_length=15)
    vehiculo_patente=models.CharField(max_length=10)

class reservaHora(models.Model):
    id_usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_reserva = models.CharField(max_length=5)
    descripcion= models.CharField(max_length=200)
    
class servicio(models.Model):
    nombre=models.CharField(max_length=25)
    precio=models.IntegerField()
    tiempo_ejecucion=models.DurationField()
    estado=models.CharField(max_length=1)
    descuento=models.IntegerField()

class producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()
    stock=models.IntegerField()
    garantia=models.IntegerField()

class ordenPedido(models.Model):
    id_usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    descripcion_pedido = models.TextField()
    cantidad_prod_pedido = models.IntegerField()
    precio_prod_unidad = models.IntegerField()

class boleta(models.Model):
    id_usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
    fecha_boleta = models.DateField()
    cantidad_boleta = models.IntegerField()
    subtotal_boleta = models.IntegerField()

class factura(models.Model):
    id_usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    cantidad_factura = models.IntegerField()
    subtotal_factura = models.IntegerField()  


    
    

      

    

