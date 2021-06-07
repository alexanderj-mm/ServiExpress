from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    
    path('listarReservaHora', login_required(views.listar_reserva_hora), name="listar_reserva_hora"),
    path('agregarReservaHora',login_required(views.agregar_reserva_hora), name="agregar_reserva_hora"),
    path('editarReservaHora/<int:id_reserva>', login_required(views.editar_reserva_hora), name="editar_reserva_hora"),
    path('eliminaReservaHora/<int:id_reserva>', login_required(views.eliminar_reserva_hora), name="eliminar_reserva_hora"),
    path('agregarServicio',login_required(views.agregar_servicio), name="agregar_servicio"),
    path('editarServicio/<int:id_servicio>', login_required(views.editar_servicio), name="editar_servicio"),
    path('eliminaServicio/<int:id_servicio>', login_required(views.eliminar_servicio), name="eliminar_servicio"), 
    path('listarServicio', login_required(views.listar_servicio), name="listar_servicio"),
    path('agregarProducto',login_required(views.agregar_producto), name="agregar_producto"),
    path('editarProducto/<int:id_producto>', login_required(views.editar_producto), name="editar_producto"),
    path('eliminaProducto/<int:id_producto>', login_required(views.eliminar_producto), name="eliminar_producto"),
    path('listarProducto', login_required(views.listar_producto), name="listar_producto"),  
    path('agregarOrdenPedido', login_required(views.agregar_orden_pedido), name="agregar_orden_pedido"),
    path('eliminaOrdenPedido/<int:id_orden_pedido>', login_required(views.eliminar_orden_pedido), name="eliminar_orden_pedido"),
    path('editarOrdenPedido/<int:id_orden_pedido>', login_required(views.editar_orden_pedido), name="editar_orden_pedido"),
    path('listarOrdenPedido', login_required(views.listar_orden_pedido), name="listar_orden_pedido"),
    path('crearBoleta', login_required(views.crear_boleta), name="crear_boleta"),
    path('listarBoleta', login_required(views.listar_boleta), name="listar_boleta"),
    path('modificarBoleta/<int:id_boleta>', login_required(views.modificar_boleta), name="modificar_boleta"),
    path('anularBoleta/<int:id_boleta>', login_required(views.anular_boleta), name="anular_boleta"),
    path('crearFactura', login_required(views.crear_factura), name="crear_factura"),
    path('listarFactura', login_required(views.listar_factura), name="listar_factura"),
    path('modificarFactura/<int:id_factura>', login_required(views.modificar_factura), name="modificar_factura"),
    path('anularFactura/<int:id_factura>', login_required(views.anular_factura), name="anular_factura"),

]
