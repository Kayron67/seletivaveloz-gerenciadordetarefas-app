from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projetos', views.ProjetoViewSet, basename='projeto')

urlpatterns = [
    path('', include(router.urls)),
]