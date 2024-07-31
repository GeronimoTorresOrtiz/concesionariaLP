from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from vehiculos.models import Vehiculo


class Factura(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='facturas'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    num_factura = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Factura {self.num_factura} - {self.cliente}"
        
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ventas'
    )
    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        related_name='ventas'
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='ventas'
    )
    
    def __str__(self):
        return f"Venta {self.factura.num_factura} - {self.cliente} - {self.vehiculo}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Venta {self.venta.factura.num_factura} - {self.descripcion}"
