from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from datetime import datetime

from vehiculos.forms import VehiculoForm, VehiculoImageForm
from vehiculos.models import VehiculoImage
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaRepository
from vehiculos.repositories.modelo import ModeloRepository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais import PaisRepository
from usuarios.models import Profile
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate
)




vehiculo_repo = VehiculoRepository()
marca_repo = MarcaRepository()
modelo_repo = ModeloRepository()
combustible_repo = CombustibleRepository()
pais_repo = PaisRepository()

class VehiculoListaView(View):
    def get(self, request):
        if not request.user.is_anonymous:
            profile= Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)
        marca_id = request.GET.get('brand')

        
        # Si se proporciona un ID de marca, filtrar los vehículos por marca
        if marca_id:
            vehiculos = vehiculo_repo.get_by_marca(marca_id)
        else:
            vehiculos = vehiculo_repo.get_all()

        marcas = marca_repo.get_all()

        return render(
            request,
            'vehiculos/list.html',
            {
                'vehicles': vehiculos,
                'lista_marcas': marcas,  
                'current_time': datetime.now().strftime('%H:%M:%S'),

            }
        )

class VehiculoDeleteView(View):
    def get(self, request, id):
        vehiculo = vehiculo_repo.get_by_id(id=id)
        vehiculo_repo.delete(vehiculo=vehiculo)
        return redirect('vehiculo_lista')

class VehiculoCreateView(View):
    def get(self, request):
        form = VehiculoForm()
        marcas = marca_repo.get_all()
        modelos = modelo_repo.get_all()
        combustibles = combustible_repo.get_all()
        paises = pais_repo.get_all()
        
        return render(
            request,
            'vehiculos/create.html',
            {
                'form': form,
                'marcas': marcas,
                'modelos': modelos,
                'combustibles': combustibles,
                'paises': paises
            }
        )

    def post(self, request):
        form = VehiculoForm(request.POST)
        if form.is_valid():
            marca_id = form.cleaned_data['marca'].id
            modelo_id = form.cleaned_data['modelo'].id
            combustible_id = form.cleaned_data['combustible'].id
            pais_id = form.cleaned_data['pais_fabricacion'].id

            marca = marca_repo.get_by_id(marca_id)
            modelo = modelo_repo.get_by_id(modelo_id)
            combustible = combustible_repo.get_by_id(combustible_id)
            pais_fabricacion = pais_repo.get_by_id(pais_id)

            vehiculo_nuevo = vehiculo_repo.create(
                marca=marca,
                modelo=modelo,
                cant_puertas=form.cleaned_data['cant_puertas'],
                cilindrada=form.cleaned_data['cilindrada'],
                combustible=combustible,
                pais_f=pais_fabricacion,
                precio=form.cleaned_data['precio_en_dolares'],
            )
            return redirect('vehiculo_lista')
        
        marcas = marca_repo.get_all()
        modelos = modelo_repo.get_all()
        combustibles = combustible_repo.get_all()
        paises = pais_repo.get_all()
        
        return render(
            request,
            'vehiculos/create.html',
            {
                'form': form,
                'marcas': marcas,
                'modelos': modelos,
                'combustibles': combustibles,
                'paises': paises
            }
        )

@method_decorator(login_required(login_url='login'), name='dispatch')
class VehiculoUpdateView(View):
    def get(self, request, id):
        vehiculo = get_object_or_404(vehiculo_repo.get_all(), id=id)
        form = VehiculoForm(instance=vehiculo)
        image_form = VehiculoImageForm()

        marcas = marca_repo.get_all()
        modelos = modelo_repo.get_all()
        combustibles = combustible_repo.get_all()
        paises = pais_repo.get_all()

        return render(
            request,
            'vehiculos/update.html',
            {
                'form': form,
                'image_form': image_form,
                'marcas': marcas,
                'modelos': modelos,
                'combustibles': combustibles,
                'paises': paises
            }
        )

    def post(self, request, id):
        vehiculo = get_object_or_404(vehiculo_repo.get_all(), id=id)
        form = VehiculoForm(request.POST, instance=vehiculo)
        image_form = VehiculoImageForm(request.POST, request.FILES)

        if form.is_valid():
            vehiculo = form.save()

            if image_form.is_valid():
                vehiculo_image = image_form.save(commit=False)
                vehiculo_image.vehiculo = vehiculo
                vehiculo_image.save()

            return redirect('vehiculo_lista')

        marcas = marca_repo.get_all()
        modelos = modelo_repo.get_all()
        combustibles = combustible_repo.get_all()
        paises = pais_repo.get_all()

        return render(
            request,
            'vehiculos/update.html',
            {
                'form': form,
                'image_form': image_form,
                'marcas': marcas,
                'modelos': modelos,
                'combustibles': combustibles,
                'paises': paises
            }
        )

class VehiculoComentariosView(View):
    def get(self, request, id):
        vehiculo = vehiculo_repo.get_by_id(id)
        comentarios = vehiculo.comentarios.all()
        return render(
            request,
            'vehiculos/comentarios.html',
            {
                'vehiculo': vehiculo,
                'comentarios': comentarios
            }
        )
