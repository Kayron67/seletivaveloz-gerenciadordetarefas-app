from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Tarefa
from django.contrib.auth import get_user_model
from core.fields import HyperlinkedNestedIdentityField

getModelUsuario = get_user_model()

class TarefaResumidaEmProjetoSerializer(serializers.ModelSerializer):
    url = HyperlinkedNestedIdentityField(
        view_name='projeto-tarefas-detail',
        parent_lookup_kwargs={'projeto_pk': 'projeto.pk'}
    )

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'concluida']

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
        queryset=getModelUsuario.objects.all(),
        required=False
    )

    projeto_info = serializers.SerializerMethodField()

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'descricao', 'data_de_entrega', 'concluida', 'projeto_info', 'prioridade', 'responsaveis']

    def get_projeto_info(self, obj):
        request = self.context.get('request')
        projeto_url = reverse('projeto-detail', kwargs={'pk': obj.projeto.pk}, request=request)
        return {
            'titulo': obj.projeto.titulo,
            'url': projeto_url
        }