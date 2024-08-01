from typing import List
from vehiculos.models import Pais

class PaisRepository:

    def get_all(self) -> List[Pais]:
        return Pais.objects.all()

    def create(
        self,
        nombre: str,
    ) -> Pais:
        return Pais.objects.create(
            name=nombre,
        )
    def delete(self, pais: Pais):
        return pais.delete()
    
    def update(
    self,
    pais: Pais,
    nombre: str,
) -> Pais:
        pais.name = nombre

        pais.save()
        return pais

