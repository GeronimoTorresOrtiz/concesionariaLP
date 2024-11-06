from django.conf import settings
import datetime

from vehiculos.models import Marca

from usuarios.models import  Profile

def profile(request):
    user_profile = None
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # En caso de que no exista un perfil para el usuario
    return {'profile': user_profile}

def lista_marcas_context(request):
    marcas = Marca.objects.all()
    return {
        'lista_marcas': marcas,
    }



def site_context(request):
    now = datetime.datetime.now()
    time_now = now.strftime('%H:%M:%S') 
    
    return {
        'SITE_NAME': settings.SITE_NAME,
        'current_year': now.year,
        'current_time': time_now, 
    }

