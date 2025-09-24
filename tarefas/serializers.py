from django.contrib.auth.models import User
from rest_framework import serializers
from.models import Tarefa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    responsaveis = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='user-detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'descricao', 'data_de_entrega', 'concluida', 'prioridade', 'responsaveis']