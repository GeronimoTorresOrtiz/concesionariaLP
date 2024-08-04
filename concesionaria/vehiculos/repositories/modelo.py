from typing import List, Optional
from vehiculos.models import Modelo

class ModeloRepository:

    def get_all(self) -> List[Modelo]:
        return Modelo.objects.all()
    
        
    def get_by_id(self, id: int) -> Optional[Modelo]:
        try:
            return Modelo.objects.get(id=id)
        except Modelo.DoesNotExist:
            return None

        

    def create(
        self,
        nombre: str,
    ) -> Modelo:
        return Modelo.objects.create(
            name=nombre,
        )
    
    def delete(self, modelo: Modelo):
        return modelo.delete()
    
    def update(
    self,
    modelo: Modelo,
    nombre: str,
) -> Modelo:
        modelo.name = nombre

        modelo.save()
        return modelo

