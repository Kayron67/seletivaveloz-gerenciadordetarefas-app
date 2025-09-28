from rest_framework import serializers
from .models import Projeto
from tarefas.serializers import TarefaResumidaEmProjetoSerializer

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    tarefas = TarefaResumidaEmProjetoSerializer(many=True, read_only=True)

    adicionar_tarefa_para_esse_projeto_url = serializers.HyperlinkedIdentityField(
        view_name='projeto-tarefas-list',
        lookup_url_kwarg='projeto_pk'
    )

    class Meta:
        model = Projeto
        fields = ['titulo', 'id', 'url',  'criador', 'descricao', 'membros', 'tarefas', 'adicionar_tarefa_para_esse_projeto_url']
        read_only_fields = ['criador']