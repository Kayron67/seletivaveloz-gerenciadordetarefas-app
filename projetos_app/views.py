from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Projeto, Fileira
from .serializers import ProjetoSerializer, FileiraSerializer
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

class FileiraViewSet(viewsets.ModelViewSet):
    serializer_class = FileiraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Fileira.objects.filter(projeto_id=self.kwargs['projeto_pk'])
    
    def perform_create(self, serializer):
        serializer.save(projeto_id=self.kwargs['projeto_pk'])