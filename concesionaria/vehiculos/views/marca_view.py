from django.shortcuts import render
from django.views import View
from vehiculos.repositories.marca import MarcaRepository

repo = MarcaRepository()

class MarcaListaView(View):
    def get(self, request):
        marcas = repo.get_all()
        return render(
            request,
            'vehiculos/create.html',
            {'marcas': marcas}
        )

class IndexView(View):
    def get(self, request):
        return render(
            request,
            'index/index.html'
        )
