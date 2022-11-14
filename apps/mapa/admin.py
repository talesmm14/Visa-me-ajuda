from django.contrib import admin

from apps.mapa.models import Mapa, Passo, PerguntaEResposta, Trilha, Link


class PassoInline(admin.TabularInline):
    model = Passo
    show_change_link = True
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


class MapaInline(admin.TabularInline):
    model = Mapa
    show_change_link = True
    verbose_name = "Mapas"
    extra = 1


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    inlines = (MapaInline,)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
