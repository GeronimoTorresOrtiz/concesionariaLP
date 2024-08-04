from typing import List, Optional
from vehiculos.models import Marca

class MarcaRepository:

    def get_all(self) -> List[Marca]:
        return Marca.objects.all()
    
    def get_by_id(self, id: int) -> Optional[Marca]:
        try:
            return Marca.objects.get(id=id)
        except Marca.DoesNotExist:
            return None

        

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
