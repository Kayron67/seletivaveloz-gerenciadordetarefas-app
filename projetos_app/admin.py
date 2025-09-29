from django.contrib import admin
from .models import Projeto, Fileira

class FileiraInlineParaProjetos(admin.TabularInline):
    model = Fileira
    extra = 1

class ProjetoAdmin(admin.ModelAdmin):
    inlines = [FileiraInlineParaProjetos]
    list_display = ('titulo', 'criador')
    search_fields = ('titulo', 'descricao')
    list_filter = ('criador', 'membros')
    filter_horizontal = ('membros',)

admin.site.register(Projeto, ProjetoAdmin)

@admin.register(Fileira)
class FileiraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'ordem')
    list_filter = ('projeto',)

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ('projeto',)
        return ()

    def has_add_permission(self, request):
        return False