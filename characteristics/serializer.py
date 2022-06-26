from rest_framework import serializers

# from .models import Characteristic


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
