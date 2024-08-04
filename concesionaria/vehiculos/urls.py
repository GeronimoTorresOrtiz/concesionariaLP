from django.urls import path

from vehiculos.views.vehiculo_view import (
    vehiculo_lista,
    vehiculo_delete,
    vehiculo_create,)

urlpatterns = [
    path(route="",view=vehiculo_lista,name='vehiculo_lista'),
    path(route="create/",view=vehiculo_create,name='vehiculo_create'),    
    path(route="<int:id>/delete/",view=vehiculo_delete,name='vehiculo_delete'),    

]