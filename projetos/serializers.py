from rest_framework import serializers
from .models import Projeto
from tarefas.serializers import TarefaResumidaEmProjetoSerializer

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    tarefas = TarefaResumidaEmProjetoSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = ['url', 'id', 'titulo', 'descricao', 'criador', 'membros', "tarefas"]
        read_only_fields = ['criador']