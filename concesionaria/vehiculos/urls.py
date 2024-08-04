from django.urls import path
from vehiculos.views.vehiculo_view import (
    vehiculo_lista,
    vehiculo_delete,
    vehiculo_create,
    vehiculo_update,
)
from vehiculos.views.comentario_view import (
    comentario_lista,
    comentario_delete,
    comentario_create,
    comentario_update
)

urlpatterns = [
    path(route="", view=vehiculo_lista, name='vehiculo_lista'),
    path(route="create/", view=vehiculo_create, name='vehiculo_create'),
    path(route="<int:id>/delete/", view=vehiculo_delete, name='vehiculo_delete'),
    path(route="<int:id>/update/", view=vehiculo_update, name='vehiculo_update'),

    path(route="<int:vehiculo_id>/comentarios/", view=comentario_lista, name='comentario_lista'),
    path(route="<int:vehiculo_id>/comentarios/create/", view=comentario_create, name='comentario_create'),
    path(route="<int:comentario_id>/comentarios/update/", view=comentario_update, name='comentario_update'),
    path(route="comentario/<int:id>/delete/", view=comentario_delete, name='comentario_delete'),
]
