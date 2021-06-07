from django.shortcuts import render, redirect
from .models import reservaHora, cliente, servicio, producto, factura, boleta, ordenPedido
from .forms import reservaHoraForm ,clienteForm, servicioForm, productoForm, facturaForm, boletaForm, ordenPedidoForm
from django.contrib.auth.models import User

# Create your views here.

def listar_servicio(request):
    if request.user.is_superuser == 1:
        instancia_servicio = servicio.objects.all().order_by('id')    
    else:
        instancia_servicio = servicio.objects.filter(id_usuario=request.user.id)
            
    return render(request, "Registro/listar_servicio.html", {'servicio': instancia_servicio})

def listar_producto(request):
    if request.user.is_superuser == 1:
        instancia_producto = producto.objects.all().order_by('id')    
    else:
        instancia_producto = producto.objects.filter(id_usuario=request.user.id)
            
    return render(request, "Registro/listar_producto.html", {'producto': instancia_producto})

def listar_orden_pedido(request):
    if request.user.is_superuser == 1:
        instancia_orden = ordenPedido.objects.all().order_by('id')  
    return render(request, "Registro/listar_orden_pedido.html", {'ordenPedido': instancia_orden})

def listar_reserva_hora(request):
    if request.user.is_superuser == 1:
        instancia_reserva = reservaHora.objects.all().order_by('id')    
    else:
        instancia_reserva = reservaHora.objects.filter(id_usuario=request.user.id)
            
    return render(request, "Registro/listar_reserva_hora.html", {'reserva': instancia_reserva})

def listar_factura(request):
    if request.user.is_superuser == 1:
        instancia_factura = factura.objects.all().order_by('id')  
    else:
        instancia_factura = factura.objects.filter(id_usuario=request.user.id)
    return render(request, "Registro/listar_factura.html", {'factura': instancia_factura})

def listar_boleta(request):
    if request.user.is_superuser == 1:
        instancia_boleta = boleta.objects.all().order_by('id')  
    else:
        instancia_boleta = boleta.objects.filter(id_usuario=request.user.id)
    return render(request, "Registro/listar_boleta.html", {'boleta': instancia_boleta})

def agregar_reserva_hora(request):
    if request.method == "POST":
        formCliente = clienteForm(request.POST)
        formReservaHora = reservaHoraForm(request.POST)       
        if formReservaHora.is_valid() and formCliente.is_valid():   
            instancia_cliente = formCliente.save(commit=False)
            instancia_cliente.id_usuario=request.user
            instancia_cliente.save()   
            instancia_reserva = formReservaHora.save(commit=False)
            instancia_reserva.id_cliente=instancia_cliente
            instancia_reserva.id_usuario=request.user     
            instancia_reserva.save()
        return redirect("/listarReservaHora")           
    else:
        formReservaHora = reservaHoraForm()
        formCliente = clienteForm()
        return render(request, "Registro/agregar_reserva_hora.html", {'formReservaHora': formReservaHora,'formCliente': formCliente})
        
    
def editar_reserva_hora(request,id_reserva):    
    instancia_reserva = reservaHora.objects.get(id=id_reserva)    
    formCliente = clienteForm(instance=instancia_reserva.id_cliente)
    formReservaHora = reservaHoraForm(instance=instancia_reserva)
    
    if request.method == "POST":
        formCliente = clienteForm(request.POST,instance=instancia_reserva.id_cliente)
        formReservaHora = reservaHoraForm(request.POST,instance=instancia_reserva)       
        if formReservaHora.is_valid() and formCliente.is_valid():
            instancia_cliente = formCliente.save(commit=False)
            instancia_cliente.save()
            instancia_reserva = formReservaHora.save(commit=False)
            instancia_reserva.save()
            
            if request.user.is_superuser == 1:
                instancia_reserva = reservaHora.objects.all().order_by('id')    
            else:
                instancia_reserva = reservaHora.objects.filter(id_usuario=request.user.id)    
            return render(request, "Registro/listar_reserva_hora.html", {'reserva': instancia_reserva})
    else:   
        return render(request, "Registro/editar_reserva_hora.html", {'formReservaHora': formReservaHora,'formCliente': formCliente})    

def eliminar_reserva_hora(request,id_reserva):   
    instancia_reserva = reservaHora.objects.get(id=id_reserva)
    instancia_cliente = cliente.objects.get(id=instancia_reserva.id_cliente_id)
    instancia_reserva.delete()
    instancia_cliente.delete()
    if request.user.is_superuser == 1:
        instancia_reserva = reservaHora.objects.all().order_by('id')    
    else:
        instancia_reserva = reservaHora.objects.filter(id_usuario=request.user.id)
    
    return render(request, "Registro/listar_reserva_hora.html", {'reserva': instancia_reserva})


def agregar_servicio(request):
    if request.method == "POST":
        formServicio = servicioForm(request.POST)       
        if formServicio.is_valid():    
            instancia_servicio = formServicio.save(commit=False)
            instancia_servicio.id_usuario=request.user     
            instancia_servicio.save()
        return redirect("/listarServicio")           
    else:
        formServicio = servicioForm()
        formCliente = clienteForm()
        return render(request, "Registro/agregar_servicio.html", {'formServicio': formServicio,'formCliente': formCliente})


def agregar_producto(request):
    if request.method == "POST": 
        formProducto = productoForm(request.POST)     
        if formProducto.is_valid():        
            instancia_producto = formProducto.save(commit=False)   
            instancia_producto.save()
        return redirect("/listarProducto")          
    else:
        formProducto = productoForm()
        return render(request, "Registro/agregar_producto.html", {'formProducto': formProducto})
    
    
def eliminar_producto(request,id_producto):   
    instancia_producto = producto.objects.get(id=id_producto)
    instancia_producto.delete()
    if request.user.is_superuser == 1:
        instancia_producto = producto.objects.all().order_by('id')    
    return render(request, "Registro/listar_producto.html", {'producto': instancia_producto})


def eliminar_servicio(request,id_servicio):   
    instancia_servicio = servicio.objects.get(id=id_servicio)
    instancia_servicio.delete()
    if request.user.is_superuser == 1:
        instancia_servicio = servicio.objects.all().order_by('id')    
    return render(request, "Registro/listar_servicio.html", {'servicio': instancia_servicio})


def editar_servicio(request,id_servicio):    
    instancia_servicio = servicio.objects.get(id=id_servicio)    
    formServicio = servicioForm(instance=instancia_servicio)
    
    if request.method == "POST":
        formServicio = servicioForm(request.POST,instance=instancia_servicio)       
        if formServicio.is_valid():
            instancia_servicio = formServicio.save(commit=False)
            instancia_servicio.save()
            if request.user.is_superuser == 1:
                instancia_servicio = servicio.objects.all().order_by('id')    
            return render(request, "Registro/listar_servicio.html", {'servicio': instancia_servicio})
    else:   
        return render(request, "Registro/editar_servicio.html", {'formServicio': formServicio})   


def editar_producto(request,id_producto):    
    instancia_producto = producto.objects.get(id=id_producto)    
    formProducto = productoForm(instance=instancia_producto)
    
    if request.method == "POST":
        formProducto = productoForm(request.POST,instance=instancia_producto )     
        if formProducto.is_valid():
            instancia_producto = formProducto.save(commit=False)
            instancia_producto.save()
            
            if request.user.is_superuser == 1:
                instancia_producto = producto.objects.all().order_by('id')       
            return render(request, "Registro/listar_producto.html", {'producto': instancia_producto})
    else:   
        return render(request, "Registro/editar_producto.html", {'formProducto': formProducto})  


def agregar_orden_pedido(request):
    if request.method == "POST":
        formOrdenPedido = ordenPedidoForm(request.POST)    
        if formOrdenPedido.is_valid():  
            instancia_ordenPedido = formOrdenPedido.save(commit=False)     
            instancia_ordenPedido.save()      
        return redirect("/listarOrdenPedido")           
    else:
        formOrdenPedido = ordenPedidoForm()
        return render(request, "Registro/agregar_orden_pedido.html", {'formOrdenPedido': formOrdenPedido})


def editar_orden_pedido(request, id_orden_pedido):    
    instancia_ordenPedido = ordenPedido.objects.get(id=id_orden_pedido)
    formOrden = ordenPedidoForm(instance=instancia_ordenPedido)
    
    if request.method == "POST":
        formOrden = ordenPedidoForm(request.POST,instance=instancia_ordenPedido)
        if formOrden.is_valid():
            instancia_ordenPedido = formOrden.save(commit=False)
            instancia_ordenPedido.save()

            if request.user.is_superuser == 1:
                instancia_ordenPedido = ordenPedido.objects.all().order_by('id')
            return render(request, "Registro/listar_orden_pedido.html", {'ordenPedido': instancia_ordenPedido})
    else:   
        return render(request, "Registro/editar_orden_pedido.html", {'formOrdenPedido': formOrden})   


def eliminar_orden_pedido(request,id_orden_pedido):   
    instancia = ordenPedido.objects.get(id=id_orden_pedido)
    instancia.delete()
    orden = ordenPedido.objects.all().order_by('id')
    return render(request, "Registro/listar_orden_pedido.html", {'ordenPedido': orden})


def crear_boleta(request):
    if request.method == "POST":
        formBoleta = boletaForm(request.POST)    
        if formBoleta.is_valid():  
            instancia_boleta = formBoleta.save(commit=False) 
            instancia_boleta.id_usuario=request.user   
            instancia_boleta.save()      
        return redirect("/listarBoleta")           
    else:
        formBoleta = boletaForm()
        return render(request, "Registro/crear_boleta.html", {'formBoleta': formBoleta})


def modificar_boleta(request,id_boleta):    
    instancia_boleta = boleta.objects.get(id=id_boleta)
    formBoleta = boletaForm(instance=instancia_boleta)
    
    if request.method == "POST":
        formBoleta = boletaForm(request.POST,instance=instancia_boleta)
        if formBoleta.is_valid():
            instancia_boleta = formBoleta.save(commit=False)
            instancia_boleta.save()

            if request.user.is_superuser == 1:
                instancia_boleta = boleta.objects.all().order_by('id')
            return render(request, "/listar_boleta.html", {'boleta': instancia_boleta})
    else:   
        return render(request, "Registro/modificar_boleta.html", {'formBoleta': formBoleta})    

def anular_boleta(request,id_boleta):   
    instancia_boleta = boleta.objects.get(id=id_boleta)
    instancia_boleta.delete()
    if request.user.is_superuser == 1:
        instancia_boleta = boleta.objects.all().order_by('id')    
    return render(request, "Registro/anular_boleta.html", {'boleta': instancia_boleta})


def crear_factura(request):
    if request.method == "POST":
        formFactura = facturaForm(request.POST)    
        if formFactura.is_valid():    
            instancia_factura = formFactura.save(commit=False) 
            instancia_factura.id_usuario=request.user  
            instancia_factura.save()      
        return redirect("/listarFactura")           
    else:
        formFactura = facturaForm()
        return render(request, "Registro/crear_factura.html", {'formFactura': formFactura})


def modificar_factura(request,id_factura):    
    instancia_factura = factura.objects.get(id=id_factura)
    formFactura = facturaForm(instance=instancia_factura)
    
    if request.method == "POST":
        formFactura = facturaForm(request.POST,instance=instancia_factura)
        if formFactura.is_valid():
            instancia_factura = formFactura.save(commit=False)
            instancia_factura.save()
            facturaO = factura.objects.all().order_by('id')
            return render(request, "/index.html", {'factura': facturaO})
    else:   
        return render(request, "Registro/modificar_factura.html", {'formFactura': formFactura}) 

def anular_factura(request,id_factura):   
    instancia_factura = factura.objects.get(id=id_factura)
    instancia_factura.delete()
    if request.user.is_superuser == 1:
        instancia_factura = factura.objects.all().order_by('id')    
    return render(request, "Registro/anular_factura.html", {'factura': instancia_factura})