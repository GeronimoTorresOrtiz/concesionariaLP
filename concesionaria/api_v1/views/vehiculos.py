from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers.vehiculo_serializer import VehiculoSerializer
from vehiculos.models import Vehiculo, Marca, Pais, Combustible, Modelo


class VehiculoViewSet(ModelViewSet): 
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        
        marca_data = data.get('marca')
        marca_name = marca_data.get('name')
        marca, created = Marca.objects.get_or_create(
                name= marca_name
        )

        
        modelo_data = data.get('modelo')    
        modelo_name = modelo_data.get('name')
        modelo, created = Modelo.objects.get_or_create(
            name=modelo_name
        ) 
        combustible_data = data.get('combustible') 
        combustible_name = combustible_data.get('name')
        combustible, created = Combustible.objects.get_or_create(
            name=combustible_name
        )

        pais_fabricacion_data= data.get('pais_fabricacion')
        pais_fabricacion_name = pais_fabricacion_data.get('name')
        pais_fabricacion, created = Pais.objects.get_or_create(
            name=pais_fabricacion_name
        )
        
        vehiculo = Vehiculo.objects.create(
            marca = marca or None,
            modelo = modelo or None ,
            cant_puertas =  data.get('cant_puertas'),
            cilindrada = data.get('cilindrada'),
            combustible = combustible or None,
            pais_fabricacion = pais_fabricacion or None,
            precio_en_dolares= data.get('precio_en_dolares'),
        )
        serializer = self.serializer_class(vehiculo)
        return Response(serializer.data)