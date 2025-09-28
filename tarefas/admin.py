from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'concluida', 'prioridade')
    list_filter = ('projeto', 'concluida', 'prioridade')
    search_fields = ('titulo', 'descricao')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('projeto',)
        return ()

    def has_add_permission(self, request):
        return False

admin.site.register(Tarefa, TarefaAdmin)