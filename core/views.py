from django.views.generic import ListView
from projetos_app.models import Projeto
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'conta/conta.html'

class HomeView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'home.html'
    context_object_name = 'projetos'
    login_url = 'login'

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(Q(criador=user) | Q(membros=user)).distinct().order_by('-id')