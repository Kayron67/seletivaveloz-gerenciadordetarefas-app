from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from tarefas_app import views as tarefas_views
from projetos_app import views as projetos_views
from usuarios_app import views as usuarios_views

router = routers.DefaultRouter()
router.register(r'projetos', projetos_views.ProjetoViewSet, basename='projeto')
router.register(r'usuarios', usuarios_views.UsuarioViewSet, basename='usuario')

projetos_router = routers.NestedSimpleRouter(router, r'projetos', lookup='projeto')
projetos_router.register(r'tarefas', tarefas_views.TarefaViewSet, basename='projeto-tarefas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(projetos_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
]