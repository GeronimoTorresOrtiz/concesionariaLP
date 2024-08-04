from typing import List,Optional
from vehiculos.models import Pais

class PaisRepository:

    def get_all(self) -> List[Pais]:
        return Pais.objects.all()
        
    def get_by_id(self, id: int) -> Optional[Pais]:
        try:
            return Pais.objects.get(id=id)
        except Pais.DoesNotExist:
            return None

        

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
