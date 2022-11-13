from rest_framework import viewsets

from apps.forum.models import Resposta
from apps.forum.serializers import RespostaSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
