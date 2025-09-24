from django.contrib import admin
from django.contrib.auth.models import User
from .models import Tarefa

# Customiza o adimin para exibir o nome User em português 
## Por ser modelo padrão não alterei ele, apenas a troca de nome por consistencia
###  
User._meta.verbose_name = 'Usuário'
User._meta.verbose_name_plural = 'Usuários'

admin.site.register(Tarefa)
