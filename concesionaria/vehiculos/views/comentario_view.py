from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from vehiculos.models import Vehiculo, Comentario  
from vehiculos.forms import ComentarioForm
from vehiculos.repositories.comentario import ComentarioRepository
from vehiculos.repositories.vehiculo import VehiculoRepository

comentario_repo = ComentarioRepository()
vehiculo_repo = VehiculoRepository()

class ComentarioListaView(View):
    def get(self, request, vehiculo_id):
        vehiculo = get_object_or_404(vehiculo_repo.get_all(), id=vehiculo_id)
        comentarios = comentario_repo.get_all().filter(vehiculo=vehiculo)

        if request.user.is_authenticated and not request.user.is_staff:
            comentarios = comentario_repo.filter(autor=request.user)

        return render(
            request,
            'comentarios/list.html',
            {
                'vehiculo': vehiculo,
                'comentarios': comentarios
            }
        )

class ComentarioCreateView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, vehiculo_id):
        form = ComentarioForm()
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        return render(
            request,
            'comentarios/create.html',
            {'form': form, 'vehiculo': vehiculo}
        )

    def post(self, request, vehiculo_id):
        form = ComentarioForm(request.POST)
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        if form.is_valid():
            try:
                comentario_repo.create(
                    autor=request.user, 
                    vehiculo=vehiculo,
                    contenido=form.cleaned_data['contenido'],
                    calificacion=form.cleaned_data['calificacion']
                )
                return redirect('comentario_lista', vehiculo_id=vehiculo_id)
            except Exception as e:
                form.add_error(None, f"Ocurrió un error al guardar el comentario: {e}")
        return render(
            request,
            'comentarios/create.html',
            {'form': form, 'vehiculo': vehiculo}
        )

class ComentarioUpdateView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        form = ComentarioForm(instance=comentario)
        return render(
            request,
            'comentarios/update.html',
            {'form': form, 'comentario': comentario}
        )

    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario_repo.update(
                comentario=comentario,
                autor=request.user,
                vehiculo=comentario.vehiculo,
                contenido=form.cleaned_data['contenido'],
                calificacion=form.cleaned_data['calificacion']
            )
            return redirect('comentario_lista', vehiculo_id=comentario.vehiculo.id)
        return render(
            request,
            'comentarios/update.html',
            {'form': form, 'comentario': comentario}
        )

class ComentarioDeleteView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def post(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        vehiculo_id = comentario.vehiculo.id
        comentario_repo.delete(comentario)
        return redirect('comentario_lista', vehiculo_id=vehiculo_id)
