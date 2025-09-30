from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Tarefa
from django.contrib.auth import get_user_model
from core.fields import HyperlinkedNestedIdentityField
from projetos_app.models import Fileira

UsuarioModel = get_user_model()

class TarefaResumidaEmProjetoSerializer(serializers.ModelSerializer):
    url = HyperlinkedNestedIdentityField(
        view_name='projeto-tarefas-detail',
        parent_lookup_kwargs={'projeto_pk': 'fileira.projeto.pk'}
    )

    class Meta:
        model = Tarefa
        fields = ['titulo', 'id', 'url', 'concluida']

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedNestedIdentityField(
        view_name='projeto-tarefas-detail',
        parent_lookup_kwargs={'projeto_pk': 'fileira.projeto.pk'}
    )

    responsaveis = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='usuario-detail',
        queryset=UsuarioModel.objects.all(),
        required=False
    )

    fileira = serializers.PrimaryKeyRelatedField(queryset=Fileira.objects.all())

    projeto_info_assosciado = serializers.SerializerMethodField()

    class Meta:
        model = Tarefa
        fields = ['titulo', 'id', 'url', 'descricao', 'projeto_info_assosciado', 'fileira', 'data_de_entrega', 'concluida', 'prioridade', 'responsaveis']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get('many', False):
            return

        if self.instance and not isinstance(self.instance, list) and hasattr(self.instance, 'projeto'):
            projeto = self.instance.projeto
            self.fields['fileira'].queryset = Fileira.objects.filter(projeto=projeto)
        elif self.context.get('view'):
            view = self.context['view']
            if 'projeto_pk' in view.kwargs:
                projeto_pk = view.kwargs['projeto_pk']
                self.fields['fileira'].queryset = Fileira.objects.filter(projeto_id=projeto_pk)

    def get_projeto_info_assosciado(self, obj):
        request = self.context.get('request')
        projeto_url = reverse('projeto-detail', kwargs={'pk': obj.projeto.pk}, request=request)
        return {
            'titulo': obj.projeto.titulo,
            'url': projeto_url
        }
    
    def validate_fileira(self, value):
        if self.instance:
            projeto_original = self.instance.fileira.projeto
            novo_projeto = value.projeto
            if projeto_original != novo_projeto:
                raise serializers.ValidationError("Não se pode mover a tarefa para a fileira de outro projeto")
        return value