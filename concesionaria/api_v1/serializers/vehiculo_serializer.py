from rest_framework import serializers
from vehiculos.models import Marca, Vehiculo, Modelo, Combustible, Pais

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('name', 'pk')
        ref_name = 'VehiculoMarcaSerializer'  # Nombre único

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('name', 'pk')
        ref_name = 'VehiculoModeloSerializer'  # Nombre único

class CombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustible
        fields = ('name', 'pk')
        ref_name = 'VehiculoCombustibleSerializer'  # Nombre único

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('name', 'pk')
        ref_name = 'VehiculoPaisSerializer'  # Nombre único

class VehiculoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    modelo = ModeloSerializer()
    combustible = CombustibleSerializer()
    pais_fabricacion = PaisSerializer()

    class Meta:
        model = Vehiculo
        fields = '__all__'

    def update(self, instance, validated_data):
        marca_data = validated_data.pop('marca', None)
        marca, _ = Marca.objects.get_or_create(**marca_data)
        
        modelo_data = validated_data.pop('modelo', None)
        modelo, _ = Modelo.objects.get_or_create(**modelo_data)
        
        combustible_data = validated_data.pop('combustible', None)
        combustible, _ = Combustible.objects.get_or_create(**combustible_data)
        
        pais_fabricacion_data = validated_data.pop('pais_fabricacion', None)
        pais_fabricacion, _ = Pais.objects.get_or_create(**pais_fabricacion_data)

        instance.marca = marca
        instance.modelo = modelo
        instance.combustible = combustible
        instance.pais_fabricacion = pais_fabricacion
        instance.cant_puertas = validated_data.get('cant_puertas', instance.cant_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.precio_en_dolares = validated_data.get('precio_en_dolares', instance.precio_en_dolares)

        instance.save()
        return instance
