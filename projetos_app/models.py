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
    membros = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='projetos_participantes',
        blank=True
    )

    def __str__(self):
        return self.titulo
    
class Fileira(models.Model):
    titulo = models.CharField(max_length=100)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='fileiras')
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        unique_together = ['projeto', 'titulo']

    def __str__(self):
        return self.titulo