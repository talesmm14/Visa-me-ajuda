from django.contrib.auth.models import User
from django.db import models


class Resposta(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.ForeignKey('Pergunta', on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.descricao
