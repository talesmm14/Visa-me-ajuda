from django.contrib.auth.models import User
from django.db import models


class Pergunta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(verbose_name="titulo", max_length=120)
    descricao = models.TextField()
    local = models.CharField(max_length=120)
    topico = models.ForeignKey('Topico', on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.titulo
