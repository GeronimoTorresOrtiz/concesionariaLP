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

    def filter(
        self,
        vehiculo: Optional[Vehiculo] = None,
        autor: Optional[str] = None,
        calificacion: Optional[int] = None
    ) -> List[Comentario]:
        queryset = Comentario.objects.all()

        if vehiculo is not None:
            queryset = queryset.filter(vehiculo=vehiculo)  # Usamos 'exact' implícitamente
        
        if autor is not None:
            queryset = queryset.filter(author=autor)  # Usamos 'exact' para el autor
        
        if calificacion is not None:
            queryset = queryset.filter(calificacion=calificacion)  # Usamos 'exact' implícitamente
        
        return list(queryset)


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