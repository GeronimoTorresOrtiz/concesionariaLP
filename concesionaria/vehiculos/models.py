from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Marca(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    
    def __str__(self):
        return self.name
    
class Modelo(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    
    def __str__(self):
        return self.name
    
class Combustible(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    
    def __str__(self):
        return self.name
    
class Pais(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))

    def __str__(self):
        return self.name

class Vehiculo(models.Model):
    marca = models.ForeignKey(
        Marca,
        on_delete=models.SET_NULL,
        related_name='marca_vehiculo',
        null=True,
        verbose_name=_("marca")
    )
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name='mod_vehiculo',
        null=True,
        verbose_name=_("modelo")
    )
    cant_puertas = models.IntegerField(
        default=0,
        verbose_name=_("cant_puertas")
    )
    cilindrada = models.FloatField(
        default=0,
        verbose_name=_("cilindrada")
    )
    combustible = models.ForeignKey(
        Combustible,
        on_delete=models.CASCADE,
        related_name='tipo_combustible',
        null=True,
        verbose_name=_("combustible")
    )
    pais_fabricacion = models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        related_name='pais',
        null=True,
        verbose_name=_("pais_fabricacion")
    )
    precio_en_dolares = models.FloatField(
        default=0,
        verbose_name=_("precio_en_dolares")
    ) 

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cilindrada}L) - ${self.precio_en_dolares}"

class Comentario(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("author")
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name=_("vehiculo")
    )
    contenido = models.TextField(
        verbose_name=_("contenido")
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("fecha_creacion")
    )
    calificacion = models.IntegerField(
        default=0,
        verbose_name=_("calificacion")
    )

    def __str__(self):
        return f"Comentario de {self.author} sobre {self.vehiculo}"

class VehiculoImage(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='imagenes',
        verbose_name=_("vehiculo")
    )
    image = models.ImageField(
        verbose_name=_("image")
    )
    ruta_imagen = models.CharField(
        max_length=200,
        default=None,
        null=True,
        verbose_name=_("ruta_imagen")
    )

    def __str__(self):
        return f"Imagen de {self.vehiculo.marca}"
