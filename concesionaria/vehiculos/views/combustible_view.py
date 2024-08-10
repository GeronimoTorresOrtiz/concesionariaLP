from django.shortcuts import render
from django.views import View
from vehiculos.models import Combustible
from vehiculos.repositories.combustible import CombustibleRepository

combustible_repo = CombustibleRepository()

class CombustibleListaView(View):
    def get(self, request):
        combustibles = combustible_repo.get_all()
        return render(
            request,
            'vehiculos/create.html',
            {'combustibles': combustibles}
        )
