from rest_framework import serializers

from apps.forum.models import Resposta


class RespostaSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.username')

    class Meta:
        model = Resposta
        fields = (
            'usuario_nome',
            'descricao',
            'dt_criacao',
        )
