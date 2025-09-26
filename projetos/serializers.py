from rest_framework import serializers
from .models import Projeto

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):

    tarefas_url = serializers.HyperlinkedIdentityField(
        view_name='projeto-tarefas-list',
        lookup_url_kwarg='projeto_pk'
    )

    class Meta:
        model = Projeto
        fields = ['url', 'id', 'titulo', 'descricao', 'criador', 'membros', "tarefas_url"]
        read_only_fields = ['criador']