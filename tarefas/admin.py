from django.contrib import admin
from django.contrib.auth.models import User
from .models import Tarefa

User._meta.verbose_name = 'Usuário'
User._meta.verbose_name_plural = 'Usuários'

admin.site.register(Tarefa)
