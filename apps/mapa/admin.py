from django.contrib import admin

from apps.mapa.models import Mapa, Passo, PerguntaEResposta


class PassoInline(admin.TabularInline):
    model = Passo
    verbose_name = "Passos"
    ordering = ('ordem',)
    extra = 3


@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'descricao',
    )
    list_filter = (
        'titulo',
        'descricao',
    )
    search_fields = (
        'titulo',
        'descricao',
    )
    inlines = (PassoInline,)


@admin.register(Passo)
class PassoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'descricao',
        'mapa',
    )
    list_filter = (
        'titulo',
        'descricao',
        'mapa',
    )
    search_fields = (
        'titulo',
        'descricao',
        'mapa_titulo',
    )


@admin.register(PerguntaEResposta)
class PerguntaERespostaAdmin(admin.ModelAdmin):
    pass
