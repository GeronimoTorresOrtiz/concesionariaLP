# vehiculos/context_processors.py
from django.conf import settings
import datetime

def site_context(request):
    now = datetime.datetime.now()
    time_now = now.strftime('%H:%M:%S')  # Formato de hora, minutos y segundos
    
    return {
        'SITE_NAME': settings.SITE_NAME,
        'current_year': now.year,
        'current_time': time_now,  # Hora actual en formato de reloj
    }
