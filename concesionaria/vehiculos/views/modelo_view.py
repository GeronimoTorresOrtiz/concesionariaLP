from django.shortcuts import render
from django.views import View
from vehiculos.repositories.modelo import ModeloRepository

repo = ModeloRepository()

class ModeloListaView(View):
    def get(self, request):
        modelos = repo.get_all()
        return render(
            request,
            'vehiculos/create.html',
            {'modelos': modelos}
        )

class IndexView(View):
    def get(self, request):
        return render(
            request,
            'index/index.html'
        )
