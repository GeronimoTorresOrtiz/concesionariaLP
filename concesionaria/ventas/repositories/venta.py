from typing import List, Optional
from ventas.models import Venta, Cliente, Factura, Vehiculo

class VentaRepository:

    def get_all(self) -> List[Venta]:
        return list(Venta.objects.all())

    def get_by_id(self, id: int) -> Optional[Venta]:
        return Venta.objects.filter(id=id).first()

    def create(
        self,
        cliente: Cliente,
        factura: Factura,
        vehiculo: Vehiculo,
        monto: float,
    ) -> Venta:
        return Venta.objects.create(
            cliente=cliente,
            factura=factura,
            vehiculo=vehiculo,
            monto=monto,
        )

    def update(
        self,
        venta: Venta,
        cliente: Optional[Cliente] = None,
        factura: Optional[Factura] = None,
        vehiculo: Optional[Vehiculo] = None,
        monto: Optional[float] = None,
    ) -> Venta:
        if cliente is not None:
            venta.cliente = cliente
        if factura is not None:
            venta.factura = factura
        if vehiculo is not None:
            venta.vehiculo = vehiculo
        if monto is not None:
            venta.monto = monto
        venta.save()
        return venta

    def delete(self, venta: Venta) -> None:
        venta.delete()
