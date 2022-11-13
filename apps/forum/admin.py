from django.contrib import admin

from apps.forum.models import Topico, Resposta, Pergunta


class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1
    ordering = ('dt_criacao',)


@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    inlines = (PerguntaInline,)


class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 1
    ordering = ('dt_criacao',)


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = (RespostaInline,)
