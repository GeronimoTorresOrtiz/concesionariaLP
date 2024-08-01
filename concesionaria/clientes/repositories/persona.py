from typing import List, Optional
from django.contrib.auth.models import User
from clientes.models import Persona

class PersonaRepository:

    def get_all(self) -> List[Persona]:
        return Persona.objects.all()

    def filter_by_id(self, id: int) -> Optional[Persona]:
        return Persona.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Persona]:
        try:
            persona = Persona.objects.get(id=id)
        except persona.DoesNotExist:
            persona = None
        return persona

    def create(
        self,
        name :name,
        apellido : apellido,
        f_nacimiento : f_nacimiento,

    ) -> Persona:
        return Persona.objects.create(
            name= name,
            apellido= apellido,
            f_nacimiento= f_nacimiento,
        )

    def delete(self, persona:Persona):
        return persona.delete()


    def update(
        self,
        persona: Persona,
        name: name,
        apellido: apellido,
        f_nacimiento:f_nacimiento,
    ) -> Vehiculo:
            persona.name= name
            persona.apellido= apellido
            persona.f_nacimiento= f_nacimiento

        persona.save()
        return persona
