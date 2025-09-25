from django.db import models
from django.conf import settings

class Projeto(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    criador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projetos_criados'
    )

    def __str__(self):
        return self.titulo