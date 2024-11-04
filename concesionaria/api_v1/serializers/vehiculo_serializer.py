from rest_framework import serializers

from vehiculos.models import Marca, Vehiculo, Modelo, Combustible,Pais


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('name','pk')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('name','pk')

class CombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustible
        fields = ('name','pk')

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('name','pk')

class VehiculoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    modelo = ModeloSerializer()
    combustible = CombustibleSerializer()
    pais_fabricacion = PaisSerializer()


    class Meta:
        model = Vehiculo
        fields = '__all__'

    def update(self, instance, validated_data):
        marca_data = validated_data.pop(
            'marca', None
        )
        marca, _= Marca.objects.get_or_create(
          **marca_data
        )
#------------------------------------------------#
        modelo_data = validated_data.pop(
            'modelo', None
        )
        modelo, _= Modelo.objects.get_or_create(
          **modelo_data
        )
#------------------------------------------------#
        combustible_data = validated_data.pop(
            'combustible', None
        )
        combustible, _= Combustible.objects.get_or_create(
          **combustible_data
        )
#------------------------------------------------#
        pais_fabricacion_data = validated_data.pop(
            'pais_fabricacion', None
        )
        pais_fabricacion, _= Pais.objects.get_or_create(
          **pais_fabricacion_data
        )
#------------------------------------------------#
        instance.marca= marca
        instance.modelo= modelo
        instance.combustible= combustible
        instance.pais_fabricacion= pais_fabricacion

        

        instance.marca = validated_data.get('marca', instance.marca)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.cant_puertas = validated_data.get('cant_puertas', instance.cant_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.combustible = validated_data.get('combustible', instance.combustible)
        instance.pais_fabricacion = validated_data.get('pais_fabricacion', instance.pais_fabricacion)
        instance.precio_en_dolares = validated_data.get('precio_en_dolares', instance.precio_en_dolares)

        instance.save()
        return instance
    
#     def create(self,validated_data):

#         marca_data = validated_data.pop(
#             'marca', None
#         )
#         marca, created = Marca.objects.get_or_create(
#             **marca_data
#         )
# #------------------------------------------------#

#         modelo_data = validated_data.pop(
#             'modelo', None
#         )
#         modelo, created = Modelo.objects.get_or_create(
#             **modelo_data
#         )
# #------------------------------------------------#

#         combustible_data = validated_data.pop(
#             'combustible', None
#         )
#         combustible, created = Combustible.objects.get_or_create(
#             **combustible_data
#         )
# #------------------------------------------------#

#         pais_fabricacion_data = validated_data.pop(
#             'pais_fabricacion', None
#         )
#         pais_fabricacion, created = Pais.objects.get_or_create(
#             **pais_fabricacion_data
#         )
        

#         vehiculo = Vehiculo.objects.create(
#             marca= marca,
#             modelo= modelo,
#             cant_puertas= validated_data['cant_puertas'],
#             cilindrada= validated_data['cilindrada'],
#             combustible= combustible,
#             pais_fabricacion= pais_fabricacion,
#             precio_en_dolares= validated_data['precio_en_dolares']
#         )
#         return vehiculo