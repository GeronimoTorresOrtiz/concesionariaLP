import csv
from django.core.management.base import BaseCommand
from vehiculos.models import Marca, Modelo, Combustible, Pais, Vehiculo

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('vehiculos.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                marca, created = Marca.objects.get_or_create(name=row['Marca'])
                modelo, created = Modelo.objects.get_or_create(name=row['Modelo'])
                combustible, created = Combustible.objects.get_or_create(name=row['Tipo de Combustible'])
                pais, created = Pais.objects.get_or_create(name=row['Pais de Fabricacion'])

                vehiculo, created = Vehiculo.objects.get_or_create(
                    marca=marca,
                    modelo=modelo,
                    cant_puertas=row['Cantidad de Puertas'],
                    cilindrada=row['Cilindrada'],
                    combustible=combustible,
                    pais_fabricacion=pais,
                    precio_en_dolares=row['Precio en dolares'],
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Vehículo {vehiculo} creado exitosamente"))
                else:
                    self.stdout.write(self.style.WARNING(f"Vehículo {vehiculo} ya existe"))
