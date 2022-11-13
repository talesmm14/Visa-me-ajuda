from rest_framework import viewsets

from apps.forum.models import Topico
from apps.forum.serializers import TopicoSerializer


class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer
