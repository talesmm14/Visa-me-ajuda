from rest_framework import serializers

from apps.forum.models import Pergunta
from apps.forum.serializers.resposta import RespostaSerializer


class PerguntaSerializer(serializers.ModelSerializer):
    resposta_set = RespostaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = (
            'titulo',
            'descricao',
            'local',
            'resposta_set',
        )
