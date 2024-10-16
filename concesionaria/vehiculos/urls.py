from django.urls import path
from vehiculos.views.vehiculo_view import (
    VehiculoListaView,
    VehiculoDeleteView,
    VehiculoCreateView,
    VehiculoUpdateView,
)
from vehiculos.views.comentario_view import (
    ComentarioListaView,
    ComentarioDeleteView,
    ComentarioCreateView,
    ComentarioUpdateView,
)
from vehiculos.views.vehiculo_image_view import (
    VehiculoImageView,
    VehiculoImageListView,
)

urlpatterns = [
    path(route="", view=VehiculoListaView.as_view(), name='vehiculo_lista'),
    path(route="create/", view=VehiculoCreateView.as_view(), name='vehiculo_create'),
    path(route="<int:id>/delete/", view=VehiculoDeleteView.as_view(), name='vehiculo_delete'),
    path(route="<int:id>/update/", view=VehiculoUpdateView.as_view(), name='vehiculo_update'),

    path(route="<int:vehiculo_id>/comentarios/", view=ComentarioListaView.as_view(), name='comentario_lista'),
    path(route="<int:vehiculo_id>/comentarios/create/", view=ComentarioCreateView.as_view(), name='comentario_create'),
    path(route="<int:comentario_id>/comentarios/update/", view=ComentarioUpdateView.as_view(), name='comentario_update'),
    path(route="comentario/<int:id>/delete/", view=ComentarioDeleteView.as_view(), name='comentario_delete'),
    path(route="vehiculo_images", view=VehiculoImageView.as_view(), name='vehiculo_images'),
    path(route="vehiculo_images/upload/", view=VehiculoImageView.as_view(), name='vehiculo_images'),
    path(route="vehiculo_images/list/", view=VehiculoImageListView.as_view(), name='images_list'),


]
