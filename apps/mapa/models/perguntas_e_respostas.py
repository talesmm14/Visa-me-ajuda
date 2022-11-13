from django.db import models


class PerguntaEResposta(models.Model):
    pergunta = models.CharField(verbose_name="Pergunta", max_length=120, unique=True)
    resposta = models.TextField(verbose_name="Resposta")

    def __str__(self):
        return self.pergunta
