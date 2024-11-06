from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # o el modelo correspondiente
        fields = '__all__'
        ref_name = 'UsuarioUserSerializer'  # Nombre único
