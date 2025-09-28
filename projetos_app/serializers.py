from rest_framework import serializers
from .models import Projeto
from tarefas_app.serializers import TarefaResumidaEmProjetoSerializer
from usuarios_app.serializers import UsuarioResumidoSerializer

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    tarefas = TarefaResumidaEmProjetoSerializer(many=True, read_only=True)

    adicionar_tarefa_para_esse_projeto_url = serializers.HyperlinkedIdentityField(
        view_name='projeto-tarefas-list',
        lookup_url_kwarg='projeto_pk'
    )

    criador = UsuarioResumidoSerializer(read_only=True)
    membros = UsuarioResumidoSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = ['titulo', 'id', 'url',  'criador', 'descricao', 'membros', 'tarefas', 'adicionar_tarefa_para_esse_projeto_url']