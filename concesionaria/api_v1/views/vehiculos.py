from rest_framework.viewsets import ModelViewSet
from api_v1.serializers.vehiculo_serializer import VehiculoSerializer
from vehiculos.models import Vehiculo


class VehiculoViewSet(ModelViewSet): 
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    