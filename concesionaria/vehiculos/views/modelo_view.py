from django.shortcuts import redirect, render

from vehiculos.models import Modelo
from vehiculos.repositories.modelo import ModeloRepository

repo = ModeloRepository()

def modelo_lista(request):
    modelo = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        dict(
            modelos= modelo
        )
    )


def index_view(request):
    return render(
        request,
        'index/index.html'    )