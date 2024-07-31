from django.contrib import admin

# Register your models here.
from vehiculos.models import (
    Marca,
    Modelo,
    Combustible,
    Pais,
    Vehiculo,
    Comentario,
    )

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Combustible)
class CombustibleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        'marca',
        'modelo',
        'cant_puertas',
        'cilindrada',
        'combustible',
        'pais_fabricacion',
        'precio_en_dolares',
    )

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'vehiculo',
        'contenido',
        'fecha_creacion',
        'calificacion',
    )
