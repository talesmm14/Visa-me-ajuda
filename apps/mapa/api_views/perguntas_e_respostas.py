from rest_framework import viewsets

from apps.mapa.models import PerguntaEResposta
from apps.mapa.serializers import PerguntaERespostaSerializer


class PerguntaERespostaViewSet(viewsets.ModelViewSet):
    queryset = PerguntaEResposta.objects.all()
    serializer_class = PerguntaERespostaSerializer
