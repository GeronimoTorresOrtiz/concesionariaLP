from django.shortcuts import redirect, render

from vehiculos.models import Marca
from vehiculos.repositories.marca import MarcaRepository

repo = MarcaRepository()

def marca_lista(request):
    marca = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        dict(
            marcas= marca
        )
    )

def index_view(request):
    return render(
        request,
        'index/index.html'    )