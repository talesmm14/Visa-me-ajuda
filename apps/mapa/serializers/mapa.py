from rest_framework import serializers

from apps.mapa.models import Mapa, Passo


class PassoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passo
        fields = (
            'ordem',
            'titulo',
            'descricao'
        )


class MapaSerializer(serializers.ModelSerializer):
    passo_set = PassoSerializer(many=True)

    class Meta:
        model = Mapa
        fields = (
            'titulo',
            'descricao',
            'passo_set',
        )

