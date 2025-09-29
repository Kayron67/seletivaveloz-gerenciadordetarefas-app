from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Usuario
from .serializers import UsuarioSerializer
from django.contrib.auth import get_user_model

UsuarioModel = get_user_model()

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioModel.objects.all().order_by('username')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]