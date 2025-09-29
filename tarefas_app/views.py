from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tarefa
from .serializers import TarefaSerializer
from projetos_app.models import Fileira

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(fileira__projeto_id=self.kwargs['projeto_pk'])
    
    def perform_create(self, serializer):
        projeto_pk = self.kwargs['projeto_pk']
        fileira_id = self.request.data.get('fileira')

        try:
            fileira = Fileira.objects.get(id=fileira_id, projeto_id=projeto_pk)
        except Fileira.DoesNotExist:
            raise serializers.ValidationError({"fileira": "A fileira não existe ou não pertence ao projeto especificado."})

        serializer.save(fileira=fileira)