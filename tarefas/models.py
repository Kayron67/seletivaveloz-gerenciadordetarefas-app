from django.db import models

class Tarefa(models.Model):
    class Prioridade(models.TextChoices):
        PRIORIDADE_BAIXA = 'B', 'Baixa'
        PRIORIDADE_MEDIA = 'M', 'Média'
        PRIORIDADE_ALTA = 'A', 'Alta'

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    prioridade = models.CharField(
        max_length=1,
        choices=Prioridade.choices,
        default=Prioridade.PRIORIDADE_MEDIA,
    )

    def __str__(self):
        return self.titulo