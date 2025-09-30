from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Fileira, Projeto
from tarefas_app.serializers import TarefaResumidaEmProjetoSerializer
from usuarios_app.serializers import UsuarioResumidoSerializer

class FileiraSerializer(serializers.ModelSerializer):
    tarefas = TarefaResumidaEmProjetoSerializer(many=True, read_only=True)
    adicionar_tarefa_para_essa_fileira_url = serializers.SerializerMethodField()

    class Meta:
        model = Fileira
        fields = ['titulo', 'id', 'ordem', 'tarefas', 'adicionar_tarefa_para_essa_fileira_url']

    def get_adicionar_tarefa_para_essa_fileira_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('projeto-tarefas-list', kwargs={'projeto_pk': obj.projeto.pk}, request=request)
    
class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    fileiras = FileiraSerializer(many=True, read_only=True)

    adicionar_fileira_para_esse_projeto_url = serializers.HyperlinkedIdentityField(
        view_name='projeto-fileiras-list',
        lookup_url_kwarg='projeto_pk'
    )

    criador = UsuarioResumidoSerializer(read_only=True)
    membros = UsuarioResumidoSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = ['titulo', 'id', 'url',  'criador', 'descricao', 'membros', 'fileiras', 'adicionar_fileira_para_esse_projeto_url']