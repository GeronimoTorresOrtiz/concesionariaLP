from typing import List, Optional
from django.contrib.auth.models import User
from clientes.models import Cliente

class ClienteRepository:

    def get_all(self) -> List[Cliente]:
        return Cliente.objects.all()

    def filter_by_id(self, id: int) -> Optional[Cliente]:
        return Cliente.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Cliente]:
        try:
            cliente = Cliente.objects.get(id=id)
        except cliente.DoesNotExist:
            cliente = None
        return cliente

    def create(
        self,
        persona: Persona,
        direccion: str,
        telefono: int,
        email: str,
        usuario: User,
    ) -> Cliente:
        return Cliente.objects.create(
            persona= persona,
            direccion= direccion,
            telefono=telefono,
            email = email,
            usuario= usuario,
        )

    def delete(self, cliente: Cliente):
        return cliente.delete()


    def update(
        self,
        cliente: Cliente,
        persona: Persona,
        direccion: str,
        telefono: int,
        email: str,
        usuario: User,
    ) -> Vehiculo:
        cliente.persona = persona
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.email = email
        cliente.usuario = usuario

        cliente.save()
        return cliente
