from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from vehiculos.forms import VehiculoImageForm
from vehiculos.models import VehiculoImage

class VehiculoImageView(View):
    def get(self, request):
       images = VehiculoImage.objects.all()
       return render(request, 
       'vehiculo_images/list.html',
       dict(
         images=images
       )
       
       )