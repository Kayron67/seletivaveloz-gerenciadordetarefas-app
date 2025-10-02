from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Projeto, Fileira
from .serializers import ProjetoSerializer, FileiraSerializer
from django.db.models import Q
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(Q(criador=user) | Q(membros=user)).distinct()

    def perform_create(self, serializer):
        projeto = serializer.save(criador=self.request.user)
        projeto.membros.add(self.request.user)

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    fields = ['titulo', 'descricao']
    template_name = 'projetos_app/projeto_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.criador = self.request.user
        response = super().form_valid(form)
        self.object.membros.add(self.request.user)
        return response

class ProjetoDetailPageView(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = 'projetos_app/projeto_detail.html'
    context_object_name = 'projeto'
    login_url = '/admin/login/'

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(Q(criador=user) | Q(membros=user)).distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projeto = self.get_object()
        membros_ids = projeto.membros.values_list('id', flat=True)
        context['usuarios_disponiveis'] = get_user_model().objects.exclude(id__in=membros_ids)
        return context

class FileiraViewSet(viewsets.ModelViewSet):
    serializer_class = FileiraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Fileira.objects.filter(projeto_id=self.kwargs['projeto_pk'])
    
    def perform_create(self, serializer):
        serializer.save(projeto_id=self.kwargs['projeto_pk'])