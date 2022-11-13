from rest_framework import viewsets

from apps.mapa.models import Mapa, Passo
from apps.mapa.serializers import MapaSerializer, PassoSerializer


class MapaViewSet(viewsets.ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer


class PassoViewSet(viewsets.ModelViewSet):
    queryset = Passo.objects.all()
    serializer_class = PassoSerializer
