from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'get_projeto', 'fileira', 'concluida', 'prioridade')
    list_filter = ('fileira__projeto', 'concluida', 'prioridade', 'fileira')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('get_projeto',)

    @admin.display(description='Projeto', ordering='fileira__projeto')
    def get_projeto(self, obj):
        return obj.fileira.projeto

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('fileira', 'get_projeto',)
        return ('get_projeto',)

    def has_add_permission(self, request):
        return False