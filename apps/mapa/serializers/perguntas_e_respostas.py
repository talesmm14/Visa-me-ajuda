from rest_framework import serializers

from apps.mapa.models import PerguntaEResposta


class PerguntaERespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerguntaEResposta
        fields = '__all__'
