from django.shortcuts import redirect, render
from vehiculos.models import Pais
from vehiculos.repositories.pais import PaisRepository

pais_repo = PaisRepository()

def pais_lista(request):
    pais = pais_repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'paises': pais}
    )
