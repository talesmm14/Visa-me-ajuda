from rest_framework import serializers

from apps.forum.models import Topico, Pergunta


class PerguntaTituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ('id', 'titulo', 'local')


class TopicoSerializer(serializers.ModelSerializer):
    pergunta_set = PerguntaTituloSerializer(many=True)

    class Meta:
        model = Topico
        fields = ('titulo', 'descricao', 'pergunta_set')
