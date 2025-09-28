from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    readonly_fields = ('projeto',)
    list_display = ('titulo', 'projeto', 'concluida', 'prioridade')
    list_filter = ('projeto', 'concluida', 'prioridade')

admin.site.register(Tarefa, TarefaAdmin)