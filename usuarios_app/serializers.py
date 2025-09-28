from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'url']

class UsuarioResumidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'usuario-detail', 'lookup_field': 'pk'}
        }