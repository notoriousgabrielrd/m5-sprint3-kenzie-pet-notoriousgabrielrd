from rest_framework import serializers

# from .models import Characteristic


class CharacteristicSerializer(serializers.Serializer):

    name = serializers.CharField()
