from django.views.generic import ListView
from projetos_app.models import Projeto
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'home.html'
    context_object_name = 'projetos'
    login_url = 'login'

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(Q(criador=user) | Q(membros=user)).distinct().order_by('-id')