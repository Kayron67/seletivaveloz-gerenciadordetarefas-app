from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Projeto
from .serializers import ProjetoSerializer
from django.db.models import Q

class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(Q(criador=user) | Q(membros=user)).distinct()

    def perform_create(self, serializer):
        projeto = serializer.save(criador=self.request.user)
        projeto.membros.add(self.request.user)