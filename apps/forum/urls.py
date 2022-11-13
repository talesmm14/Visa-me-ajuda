from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.forum.api_views import TopicoViewSet, PerguntaViewSet, RespostaViewSet

router = DefaultRouter()
router.register('topicos', TopicoViewSet, basename="topicos_forum")
router.register('perguntas', PerguntaViewSet, basename="perguntas_forum")
router.register('respostas', RespostaViewSet, basename="respostas_forum")

urlpatterns = [
    path('', include(router.urls)),
]
