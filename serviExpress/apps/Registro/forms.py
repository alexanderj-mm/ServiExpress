from django import forms
from .models import reservaHora ,cliente, servicio, producto, factura, boleta, ordenPedido

class reservaHoraForm(forms.ModelForm):
    class Meta:
        model = reservaHora
        fields = ['id_cliente','fecha_reserva', 'hora_reserva','descripcion']

        labels = {
            'id_cliente': 'id cliente',
            'fecha_reserva': 'Fecha reserva',
            'hora_reserva': 'Hora reserva',
            'descripcion' : 'Descripción',

        }
        widgets = {
            'id_cliente': forms.HiddenInput(),
            'fecha_reserva': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
            'hora_reserva': forms.TextInput(attrs={'type': 'time','class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows':4, 'cols':15,'class': 'form-control'}),
           
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['id_usuario','vehiculo_marca','vehiculo_modelo','vehiculo_patente']

        labels = {
            
            'id_usuario': 'id usuario',
            'vehiculo_marca': 'Marca de vehiculo',
            'vehiculo_modelo': 'Modelo de vehiculo',
            'vehiculo_patente': 'Patente de vehiculo',

        }
        widgets = {
            
            'id_usuario': forms.HiddenInput(),
            'vehiculo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo_patente': forms.TextInput(attrs={'class': 'form-control'}),
           
        }        

class servicioForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = ['nombre','precio','tiempo_ejecucion','estado','descuento']

        labels = {

            'nombre': 'Nombre servicio',
            'precio': 'Precio servicio',
            'tiempo_ejecucion' : 'Tiempo de demora estimado',
            'estado' : 'Estado actual',
            'descuento' : 'Descuento',

        }
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'type': 'integer','class': 'form-control'}),
            'tiempo_ejecucion': forms.TextInput(attrs={'type': 'time','class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento': forms.TextInput(attrs={'type': 'integer','class': 'form-control'}),
           
        }


class productoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre','precio','stock','garantia']

        labels = {

            'nombre': 'Nombre servicio',
            'precio': 'Precio servicio',
            'stock' : 'Cantidad disponible',
            'garantia' : 'Días de garantía',

        }
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'type': 'integer','class': 'form-control'}),
            'stock': forms.TextInput(attrs={'type': 'integer','class': 'form-control'}),
            'garantia': forms.TextInput(attrs={'type': 'integer','class': 'form-control'}),
           
        }

class ordenPedidoForm(forms.ModelForm):
    class Meta:
        model = ordenPedido
        fields = ['fecha_pedido', 'descripcion_pedido', 'cantidad_prod_pedido', 'precio_prod_unidad']        

        labels = {
            'fecha_pedido': 'Fecha de solicitud',
            'descripcion_pedido': 'Descripción',
            'cantidad_prod_pedido': 'Cantidad',
            'precio_prod_unidad': 'Precio por Unidad',
        }

        widgets = {
            'fecha_pedido': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
            'descripcion_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_prod_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_prod_unidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class boletaForm(forms.ModelForm):
    class Meta:
        model = boleta
        fields = ['fecha_boleta', 'cantidad_boleta', 'subtotal_boleta']        

        labels = {
            'fecha_boleta': 'Fecha de solicitud',
            'cantidad_boleta': 'Cantidad',
            'subtotal_boleta': 'SubTotal'
        }

        widgets = {
            'fecha_boleta': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
            'cantidad_boleta': forms.NumberInput(),
            'subtotal_boleta': forms.NumberInput(),
        }

class facturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = ['fecha_factura', 'cantidad_factura', 'subtotal_factura']        

        labels = {
            'fecha_factura': 'Fecha de solicitud',
            'cantidad_factura': 'Cantidad',
            'subtotal_factura': 'SubTotal'
        }

        widgets = {
            'fecha_factura': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
            'cantidad_factura': forms.NumberInput(),
            'subtotal_factura': forms.NumberInput(),
        }