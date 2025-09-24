from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer, UsuarioSerializer

getModelUsuario = get_user_model()

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = getModelUsuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer