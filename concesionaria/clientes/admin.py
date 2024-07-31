from django.contrib import admin

# Register your models here.
from clientes.models import (
    Persona,
    Cliente,
)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'apellido',
        'f_nacimiento',
    )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'persona',
        'direccion',
        'telefono',
        'email',
        'usuario',
    )
