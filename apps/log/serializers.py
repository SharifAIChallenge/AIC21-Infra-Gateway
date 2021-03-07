from rest_framework import serializers


class GameLogSerializer(serializers.Serializer):
    game_id = serializers.CharField(required=True)


class PlayerLogSerializer(serializers.Serializer):
    game_id = serializers.CharField(required=True)
    player_id = serializers.CharField(required=True)
