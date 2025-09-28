from django.contrib import admin
from .models import Projeto
from tarefas.models import Tarefa

class TarefaInlineParaProjetos(admin.TabularInline):
    model = Tarefa
    fields = ('titulo',)
    extra = 1
    show_change_link = True

class ProjetoAdmin(admin.ModelAdmin):
    inlines = [TarefaInlineParaProjetos]
    list_display = ('titulo', 'criador')
    search_fields = ('titulo', 'descricao')

admin.site.register(Projeto, ProjetoAdmin)