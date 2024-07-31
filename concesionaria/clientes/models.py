from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Persona(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    f_nacimiento = models.DateField()  
    
    def __str__(self):
        return f"{self.name} {self.apellido}"


class Cliente(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.SET_NULL,
        related_name='clientes',
        null=True
    )
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.persona)
    
