from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tarefa
from .serializers import TarefaSerializer, UsuarioSerializer

getModelUsuario = get_user_model()

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = getModelUsuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(projeto=self.kwargs['projeto_pk'])
    
    def perform_create(self, serializer):
        serializer.save(projeto_id=self.kwargs['projeto_pk'])