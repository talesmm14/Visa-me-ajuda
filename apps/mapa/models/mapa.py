

from django.db import models


class Trilha(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=120, unique=True)
    imagem = models.ImageField(blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Mapa(models.Model):
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(verbose_name="Titulo", max_length=120, unique=True)
    imagem = models.ImageField(blank=True, null=True)
    ordem = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        unique_together = ['trilha', 'ordem']


class Link(models.Model):
    link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True
    )
    imagem = models.ImageField(blank=True, null=True)


class Passo(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=120)
    descricao = models.TextField()
    imagem = models.ImageField(blank=True, null=True)
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField()
    links = models.ManyToManyField(Link, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}, {self.mapa.titulo}"

    class Meta:
        unique_together = ['mapa', 'ordem']
