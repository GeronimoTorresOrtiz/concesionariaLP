from django import forms
from .models import Vehiculo, Comentario, VehiculoImage

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'cant_puertas', 'cilindrada', 'combustible', 'pais_fabricacion', 'precio_en_dolares']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'modelo': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'cant_puertas': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),               
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
            'combustible': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'pais_fabricacion': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'precio_en_dolares': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
        }

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
        fields = ['image',]
