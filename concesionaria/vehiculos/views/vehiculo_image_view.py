import os
import tempfile
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from vehiculos.forms import VehiculoImageForm
from vehiculos.models import VehiculoImage

from vehiculos.repositories.s3 import S3Repository


class VehiculoImageView(View):
    def get(self, request):
       images = VehiculoImage.objects.all()
       form = VehiculoImageForm()
       return render(request, 
       'vehiculo_images/upload.html',
       dict(
         images=images,
         form=form,
       )
       
       )
 
    def post(self, request):
      s3_repository=S3Repository()
      form = VehiculoImageForm(request.POST, request.FILES)

      if form.is_valid():
          vehiculo = form.cleaned_data['vehiculo']
          image = form.cleaned_data['image']

          with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in image.chunks():
              temp_file.write(chunk)
            temp_file_path = temp_file.name

            image_object = VehiculoImage.objects.create(
              vehiculo= vehiculo,
              image=image,
            )
            image_object.save()
            nombre_imagen = f'imagen_vehiculo_{image_object.id}'

            s3_repository.upload_file(
              temp_file_path, 'itec-tercero', nombre_imagen
              )
      return redirect('vehiculo_images')
       

class VehiculoImageListView(View):
    def get(self, request):
       images = VehiculoImage.objects.all()
       return render(request, 
       'vehiculo_images/list.html',
       dict(
         images=images,
       )
       
       )