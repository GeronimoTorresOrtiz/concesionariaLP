from typing import List, Optional
from vehiculos.models import Vehiculo, Marca, Pais, Combustible, Modelo

class VehiculoRepository:

    def get_all(self) -> List[Vehiculo]:
        return Vehiculo.objects.all()

    def filter_by_id(self, id: int) -> Optional[Vehiculo]:
        return Vehiculo.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Vehiculo]:
        try:
            vehiculo = Vehiculo.objects.get(id=id)
        except Vehiculo.DoesNotExist:
            vehiculo = None
        return vehiculo

    def get_vehiculo_on_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Vehiculo]:
        vehiculos = Vehiculo.objects.filter(
            precio_en_dolares__range=(min_price, max_price)
        )
        return vehiculos

    def create(
        self,
        marca: Marca,
        precio: float,
        cilindrada: float,
        cant_puertas: int,
        modelo: Optional[Modelo] = None,
        combustible: Optional[Combustible] = None,
        pais_f: Optional[Pais] = None,
    ) -> Vehiculo:
        return Vehiculo.objects.create(
            marca=marca,
            precio_en_dolares=precio,
            modelo=modelo,
            combustible=combustible,
            pais_fabricacion=pais_f,
            cilindrada=cilindrada,
            cant_puertas=cant_puertas,  
        )

    def filter_by_marca(
        self,
        marca: Marca,
    ) -> List[Vehiculo]:
        return Vehiculo.objects.filter(marca=marca)
    
    def get_by_marca(self, marca_id: int) -> List[Vehiculo]:
        return Vehiculo.objects.filter(marca_id=marca_id)


    def delete(self, vehiculo: Vehiculo):
        return vehiculo.delete()

    def update(
        self,
        vehiculo: Vehiculo,
        marca: Marca,
        precio: float,
        cilindrada: float,
        cant_puertas: int,
        modelo: Optional[Modelo] = None,
        combustible: Optional[Combustible] = None,
        pais_f: Optional[Pais] = None,
    ) -> Vehiculo:
        vehiculo.marca = marca
        vehiculo.precio_en_dolares = precio
        vehiculo.modelo = modelo
        vehiculo.combustible = combustible
        vehiculo.pais_fabricacion = pais_f
        vehiculo.cilindrada = cilindrada
        vehiculo.cant_puertas = cant_puertas

        vehiculo.save()
        return vehiculo
