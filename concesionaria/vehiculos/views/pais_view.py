from django.shortcuts import render
from django.views import View
from vehiculos.repositories.pais import PaisRepository

pais_repo = PaisRepository()

class PaisListaView(View):
    def get(self, request):
        paises = pais_repo.get_all()
        return render(
            request,
            'vehiculos/create.html',
            {'paises': paises}
        )
