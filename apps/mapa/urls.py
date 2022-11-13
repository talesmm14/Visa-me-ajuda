from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.mapa.api_views import MapaViewSet, PerguntaERespostaViewSet

router = DefaultRouter()
router.register('mapas', MapaViewSet, basename="mapas_fluxo")
router.register('perguntas', PerguntaERespostaViewSet, basename="perguntas_fluxo")

urlpatterns = [
    path('', include(router.urls)),
]
