from django import forms
from .models import Vehiculo, Comentario, VehiculoImage

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'cant_puertas', 'cilindrada', 'combustible', 'pais_fabricacion', 'precio_en_dolares']

class ComentarioForm(forms.ModelForm):
    class Meta:
        CALIFICACION_CHOICES = [(i, str(i)) for i in range(1, 6)]
        model = Comentario
        fields = ['contenido', 'calificacion']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control custom-class', 'rows': 4}),
            'calificacion': forms.Select(choices=CALIFICACION_CHOICES, attrs={'class': 'form-control custom-class'}),
        }

class VehiculoImageForm(forms.ModelForm):
    class Meta:
        model = VehiculoImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control  custom-class'}),
        }

