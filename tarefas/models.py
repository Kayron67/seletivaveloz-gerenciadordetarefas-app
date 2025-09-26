from django.db import models
from django.conf import settings

class Tarefa(models.Model):
    class Prioridade(models.TextChoices):
        PRIORIDADE_BAIXA = 'B', 'Baixa'
        PRIORIDADE_MEDIA = 'M', 'Média'
        PRIORIDADE_ALTA = 'A', 'Alta'

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_de_entrega = models.DateField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    projeto = models.ForeignKey('projetos.Projeto', on_delete=models.CASCADE, related_name='tarefas')
    prioridade = models.CharField(
        max_length=1,
        choices=Prioridade.choices,
        default=Prioridade.PRIORIDADE_MEDIA,
    )
    responsaveis = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tarefas')

    def __str__(self):
        return self.titulo