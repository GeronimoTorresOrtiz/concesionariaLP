from typing import List
from vehiculos.models import Modelo

class ModeloRepository:

    def get_all(self) -> List[Modelo]:
        return Modelo.objects.all()

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

