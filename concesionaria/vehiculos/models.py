from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Marca(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.name
    
class Modelo(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.name
    
class Combustible(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.name
    
class Pais(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Vehiculo(models.Model):
    marca= models.ForeignKey(
        Marca,
        on_delete=models.SET_NULL,
        related_name='marca_vehiculo',
        null=True,
    )
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name='mod_vehiculo',
        null=True,
    )
    cant_puertas = models.IntegerField(default=0)
    cilindrada = models.FloatField(default= 0)
    combustible= models.ForeignKey(
        Combustible,
        on_delete=models.CASCADE,
        related_name='tipo_combustible',
        null=True,
    )
    
    pais_fabricacion= models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        related_name='pais',
        null=True,
    )

    precio_en_dolares = models.FloatField(default=0) 

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cilindrada}L) - ${self.precio_en_dolares}"


class Comentario(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    calificacion = models.IntegerField(default=0)

    def __str__(self):
        return f"Comentario de {self.author} sobre {self.vehiculo}"