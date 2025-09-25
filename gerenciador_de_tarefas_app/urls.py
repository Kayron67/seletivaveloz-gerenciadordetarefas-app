from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tarefas import views as tarefas_views
from projetos import views as projetos_views

router = DefaultRouter()
router.register(r'tarefas', tarefas_views.TarefaViewSet, basename='tarefa')
router.register(r'usuarios', tarefas_views.UsuarioViewSet, basename='usuario')
router.register(r'projetos', projetos_views.ProjetoViewSet, basename='projeto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
]