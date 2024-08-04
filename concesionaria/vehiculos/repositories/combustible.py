from typing import List, Optional
from vehiculos.models import Combustible

class CombustibleRepository:

    def get_all(self) -> List[Combustible]:
        return Combustible.objects.all()
        
    def get_by_id(self, id: int) -> Optional[Combustible]:
        try:
            return Combustible.objects.get(id=id)
        except Combustible.DoesNotExist:
            return None

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

