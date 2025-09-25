from django.conf import settings
from rest_framework import serializers
from.models import Tarefa
from django.contrib.auth import get_user_model

getModelUsuario = get_user_model()

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getModelUsuario
        fields = ['url', 'username', 'email']

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    responsaveis = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='usuario-detail',
        queryset=getModelUsuario.objects.all()
    )

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'descricao', 'data_de_entrega', 'concluida', 'projeto', 'prioridade', 'responsaveis']