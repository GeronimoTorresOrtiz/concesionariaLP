from rest_framework import serializers

from product.models import Marca, Vehiculo


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('name','pk')

class VehiculoSerializer(serializers.ModelSerializer):
    Marca = MarcaSerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = '__all__'

    def get_description(self, value):
        if value.description is None:
            return "No posee descripción"
        return value.description

    def update(self, instance, validated_data):
        marca_data = validated_data.pop(
            'marca', None
        )
        marca, _= Marca.objects.get_or_create(
          **marca_data
        )

        instance.marca= marca

        instance.marca = validated_data.get('marca', instance.marca)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.cant_puertas = validated_data.get('cant_puertas', instance.cant_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.combustible = validated_data.get('combustible', instance.combustible)
        instance.pais_fabricacion = validated_data.get('pais_fabricacion', instance.pais_fabricacion)
        instance.precio_en_dolares = validated_data.get('precio_en_dolares', instance.precio_en_dolares)

        instance.save()
        return instance
    