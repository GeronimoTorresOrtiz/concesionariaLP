from django.contrib import admin

# Register your models here.
from ventas.models import (
    Factura,
    Venta,
    DetalleVenta,)

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'fecha',
        'total',
        'num_factura',
    )
    
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'cliente',
        'factura',
        'monto',
        'vehiculo',
    )
    
@admin.register(DetalleVenta)
class DetalleAdmin(admin.ModelAdmin):
    list_display = (
        'venta',
        'descripcion',
        'cantidad',
        'precio_unitario',
        'subtotal',
    )