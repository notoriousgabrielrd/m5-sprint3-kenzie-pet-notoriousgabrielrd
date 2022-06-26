from rest_framework import serializers
from animals.models import Animal

from characteristics.models import Characteristic

from groups.models import Group

# from .models import Animal
from groups.serializer import GroupSerializer
from characteristics.serializer import CharacteristicSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
    # print(f">>>\n{group}\n")
    # print(f">>>\n{characteristic}\n")

    def create(self, validated_data: dict):
        # print(f">>>\n{validated_data}\n")

        valid_group = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")

        # animal
        new_group, _ = Group.objects.get_or_create(**valid_group)

        animal = Animal.objects.create(**validated_data, group=new_group)

        for item in characteristics:

            new_characteristic, _ = Characteristic.objects.get_or_create(**item)
            animal.characteristics.add(new_characteristic)

        return animal

    def update(self, instance: Animal, validated_data: dict):
        # print(f">>>\n{instance}\n")
        # print(f">>>\n{validated_data}\n")

        non_editable_keys = ("sex", "group", "characteristics")

        for key, value in validated_data.items():
            if key in non_editable_keys:
                # print(f"aqui{key}")
                raise KeyError
            setattr(instance, key, value)

        instance.save()

        return instance
