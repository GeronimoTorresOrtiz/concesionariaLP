from typing import List
from vehiculos.models import Marca

class MarcaRepository:

    def get_all(self) -> List[Marca]:
        return Marca.objects.all()

    def create(
        self,
        nombre: str,
    ) -> Marca:
        return Marca.objects.create(
            name=nombre,
        )


    def delete(self, marca: Marca):
        return marca.delete()

    def update(
    self,
    marca: Marca,
    nombre: str,
) -> Marca:
        marca.name = nombre

        marca.save()
        return marca
