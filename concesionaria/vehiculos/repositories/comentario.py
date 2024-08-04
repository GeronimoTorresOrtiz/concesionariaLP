from typing import List, Optional
from vehiculos.models import Comentario,Vehiculo

class ComentarioRepository:

    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()
    
        
    def get_by_id(self, id: int) -> Optional[Comentario]:
        try:
            return Comentario.objects.get(id=id)
        except Comentario.DoesNotExist:
            return None

    def create(
        self,
        autor: str,
        vehiculo: Optional[Vehiculo],
        contenido: str,
        calificacion: int,
    ) -> Comentario:
        return Comentario.objects.create(
            author=autor,
            vehiculo=vehiculo,
            contenido=contenido,
            calificacion=calificacion,
        )

    def delete(self, comentario: Comentario):
        return comentario.delete()

    def update(
    self,
    comentario: Comentario,
    autor: str,
    vehiculo: Optional[Vehiculo],
    contenido: str,
    calificacion: int,

) -> Comentario:
        comentario.author = autor
        comentario.vehiculo = vehiculo
        comentario.contenido = contenido
        comentario.calificacion = calificacion

        comentario.save()
        return comentario