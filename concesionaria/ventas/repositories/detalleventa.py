from typing import List, Optional
from ventas.models import DetalleVenta, Venta

class DetalleRepository:

    def get_all(self) -> List[DetalleVenta]:
        return list(DetalleVenta.objects.all())

    def get_by_id(self, id: int) -> Optional[DetalleVenta]:
        return DetalleVenta.objects.filter(id=id).first()

    def create(
        self,
        venta: Venta,
        description: str,
        cantidad: int,
        precio_unitario: float,
        subtotal: float,
    ) -> DetalleVenta:
        return DetalleVenta.objects.create(
            venta=venta,
            description=description,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            subtotal=subtotal,
        )

    def delete(self, detalleVenta: DetalleVenta) -> None:
        detalleVenta.delete()

    def update(
        self,
        detalle: DetalleVenta,
        description: str,
        cantidad: int,
        precio_unitario: float,
        subtotal: float,
    ) -> DetalleVenta:
        detalle.description = description
        detalle.cantidad = cantidad
        detalle.precio_unitario = precio_unitario
        detalle.subtotal = subtotal
        detalle.save()
        return detalle

