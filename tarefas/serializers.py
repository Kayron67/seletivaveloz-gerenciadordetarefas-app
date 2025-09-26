from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth import get_user_model
from core.fields import HyperlinkedNestedIdentityField

getModelUsuario = get_user_model()

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getModelUsuario
        fields = ['url', 'username', 'email']

class TarefaSerializer(serializers.HyperlinkedModelSerializer):

    url = HyperlinkedNestedIdentityField(
        view_name='projeto-tarefas-detail',
        parent_lookup_kwargs={'projeto_pk': 'projeto.pk'}
    )

    responsaveis = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='usuario-detail',
        queryset=getModelUsuario.objects.all()
    )

    projeto = serializers.HyperlinkedRelatedField(
        view_name='projeto-detail',
        read_only=True,
    )

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'descricao', 'data_de_entrega', 'concluida', 'projeto', 'prioridade', 'responsaveis']
        read_only_fields = ['projeto']