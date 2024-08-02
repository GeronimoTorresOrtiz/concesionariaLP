from typing import List, Optional
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from clientes.models import Persona
from datetime import date

class PersonaRepository:

    def get_all(self) -> QuerySet[Persona]:
        return Persona.objects.all()

    def filter_by_id(self, id: int) -> Optional[Persona]:
        return Persona.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Persona]:
        try:
            persona = Persona.objects.get(id=id)
        except Persona.DoesNotExist:  # Corregido aquí
            persona = None
        return persona

    def create(
        self,
        name: str,
        apellido: str,
        f_nacimiento: date,
    ) -> Persona:
        return Persona.objects.create(
            name=name,
            apellido=apellido,
            f_nacimiento=f_nacimiento,
        )

    def delete(self, persona: Persona):
        return persona.delete()

    def update(
        self,
        persona: Persona,
        name: str,
        apellido: str,
        f_nacimiento: date,
    ) -> Persona:  # Corregido aquí
        persona.name = name
        persona.apellido = apellido
        persona.f_nacimiento = f_nacimiento

        persona.save()
        return persona
