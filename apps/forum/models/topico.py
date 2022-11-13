from django.db import models


class Topico(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=120)
    descricao = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=120, blank=True, null=True)
    dt_criacao = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.titulo
