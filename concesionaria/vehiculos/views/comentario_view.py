from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from vehiculos.models import Vehiculo, Comentario
from vehiculos.forms import ComentarioForm
from vehiculos.repositories.comentario import ComentarioRepository
from vehiculos.repositories.vehiculo import VehiculoRepository

comentario_repo = ComentarioRepository()
vehiculo_repo = VehiculoRepository()

@login_required
def comentario_lista(request, vehiculo_id):
    vehiculo = get_object_or_404(vehiculo_repo.get_all(), id=vehiculo_id)
    comentarios = comentario_repo.get_all().filter(vehiculo=vehiculo)
    return render(
        request,
        'vehiculos/comentarios.html',
        {
            'vehiculo': vehiculo,
            'comentarios': comentarios
        }
    )

@login_required
def comentario_create(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_repo.create(
                autor=request.user,  # Assuming the author is the currently logged-in user
                vehiculo=vehiculo,
                contenido=form.cleaned_data['contenido'],
                calificacion=form.cleaned_data['calificacion']
            )
            return redirect('comentario_lista', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioForm()

    return render(
        request,
        'vehiculos/comentario_create.html',
        {
            'form': form,
            'vehiculo': vehiculo
        }
    )

@login_required
def comentario_update(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario_repo.update(
                comentario=comentario,
                autor=request.user,  # Assuming the author is the currently logged-in user
                vehiculo=comentario.vehiculo,
                contenido=form.cleaned_data['contenido'],
                calificacion=form.cleaned_data['calificacion']
            )
            return redirect('comentario_lista', vehiculo_id=comentario.vehiculo.id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(
        request,
        'vehiculos/comentario_update.html',
        {
            'form': form,
            'comentario': comentario
        }
    )

@login_required
def comentario_delete(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    vehiculo_id = comentario.vehiculo.id 
    if request.method == 'POST':
        comentario_repo.delete(comentario)
        return redirect('comentario_lista', vehiculo_id=vehiculo_id)
    return redirect('comentario_lista', vehiculo_id=vehiculo_id)