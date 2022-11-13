from django.db import models


class Mapa(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=120, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Passo(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=120)
    descricao = models.TextField()
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo}, {self.mapa.titulo}"

    class Meta:
        unique_together = ['mapa', 'ordem']
