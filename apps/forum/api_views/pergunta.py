from rest_framework import viewsets

from apps.forum.models import Pergunta
from apps.forum.serializers import PerguntaSerializer


class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer
