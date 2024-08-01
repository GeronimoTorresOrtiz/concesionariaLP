from typing import List
from vehiculos.models import Combustible

class CombustibleRepository:

    def get_all(self) -> List[Combustible]:
        return Combustible.objects.all()

    def create(
        self,
        nombre: str,
    ) -> Combustible:
        return Combustible.objects.create(
            name=nombre,
        )
    
    def delete(self, combustible: Combustible):
        return combustible.delete()
    
    def update(
    self,
    combustible: Combustible,
    nombre: str,
) -> Combustible:
        combustible.name = nombre

        combustible.save()
        return combustible

