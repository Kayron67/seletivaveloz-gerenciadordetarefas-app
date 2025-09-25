from rest_framework import serializers
from .models import Projeto

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projeto
        fields = ['url', 'id', 'titulo', 'descricao', 'criador', 'membros', 'tarefas']
        read_only_fields = ['criador', 'tarefas']