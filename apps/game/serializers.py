from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(max_length=256, allow_null=True,
                                  allow_blank=True)


class GameRegisterSerializer(serializers.Serializer):
    player_ids = StringListField()
    map_id = serializers.CharField(max_length=128)
