from rest_framework import serializers

from apps.mapa.models import Mapa, Passo, Trilha, Link


class LinkSerializer(serializers.ModelSerializer):
    link = serializers.URLField()

    class Meta:
        model = Link
        fields = '__all__'


class PassoSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = Passo
        fields = (
            'id',
            'ordem',
            'titulo',
            'imagem',
            'descricao',
            'links',
        )


class MapaSerializer(serializers.ModelSerializer):
    passo_set = PassoSerializer(many=True)

    class Meta:
        model = Mapa
        fields = (
            'id',
            'titulo',
            'descricao',
            'imagem',
            'passo_set',
        )


class TrilhaSerializer(serializers.ModelSerializer):
    mapa_set = MapaSerializer(many=True)

    class Meta:
        model = Trilha
        fields = (
            'id',
            'titulo',
            'descricao',
            'imagem',
            'mapa_set',
        )
