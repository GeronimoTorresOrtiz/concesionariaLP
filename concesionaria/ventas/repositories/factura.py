from typing import List, Optional
from facturas.models import Factura
from clientes.models import Cliente

class FacturaRepository:

    def get_all(self) -> List[Factura]:
        return list(Factura.objects.all())

    def get_by_id(self, id: int) -> Optional[Factura]:
        return Factura.objects.filter(id=id).first()

    def create(
        self,
        cliente: Cliente,
        num_factura: str,
        total: float,
    ) -> Factura:
        return Factura.objects.create(
            cliente=cliente,
            num_factura=num_factura,
            total=total,
        )

    def update(
        self,
        factura: Factura,
        cliente: Cliente,
        num_factura: str,
        total: float,
    ) -> Factura:
        factura.cliente = cliente
        factura.num_factura = num_factura
        factura.total = total
        factura.save()
        return factura

    def delete(self, factura: Factura) -> None:
        factura.delete()
