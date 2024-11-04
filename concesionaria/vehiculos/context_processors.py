from django.conf import settings
import datetime

from vehiculos.models import Marca

from usuarios.models import  Profile


def profile(request):
    return dict(
        profile= Profile.objects.get(user=request.user)
    )

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

