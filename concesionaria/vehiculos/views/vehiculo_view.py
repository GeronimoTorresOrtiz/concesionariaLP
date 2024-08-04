# vehiculos/views.py
from django.shortcuts import redirect, render
from vehiculos.forms import VehiculoForm
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaRepository
from vehiculos.repositories.modelo import ModeloRepository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais import PaisRepository

vehiculo_repo = VehiculoRepository()
marca_repo = MarcaRepository()
modelo_repo = ModeloRepository()
combustible_repo = CombustibleRepository()
pais_repo = PaisRepository()

def vehiculo_lista(request):
    vehiculos = vehiculo_repo.get_all()
    return render(
        request,
        'vehiculos/list.html',
        {'vehicles': vehiculos}
    )

def vehiculo_delete(request, id):
    vehiculo = vehiculo_repo.get_by_id(id=id)
    vehiculo_repo.delete(vehiculo=vehiculo)
    return redirect('vehiculo_lista')

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            # Guarda los objetos relacionados si aún no están guardados
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
    else:
        form = VehiculoForm()
    
    marcas = marca_repo.get_all()  # Obtener todas las marcas
    modelos = modelo_repo.get_all()  # Obtener todos los modelos
    combustibles = combustible_repo.get_all()  # Obtener todos los combustibles
    paises = pais_repo.get_all()  # Obtener todos los países
    
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

def index_view(request):
    return render(
        request,
        'index/index.html'
    )
