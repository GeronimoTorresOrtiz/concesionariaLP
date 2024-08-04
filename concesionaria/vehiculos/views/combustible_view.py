from django.shortcuts import redirect, render
from vehiculos.models import Combustible
from vehiculos.repositories.combustible import CombustibleRepository

combustible_repo = CombustibleRepository()

def combustible_lista(request):
    combustible = combustible_repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'combustibles': combustible}
    )


