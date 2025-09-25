from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Projeto
from .serializers import ProjetoSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticated]

def perform_create(self, serializer):
    serializer.save(criador=self.request.user)