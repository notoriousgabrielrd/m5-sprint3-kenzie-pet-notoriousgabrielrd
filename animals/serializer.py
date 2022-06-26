from rest_framework import serializers
from animals.models import Animal

from characteristics.models import Characteristic

from groups.models import Group

# from .models import Animal
from groups.serializer import GroupSerializer
from characteristics.serializer import CharacteristicSerializer


class AnimalSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
    # print(f">>>\n{group}\n")
    # print(f">>>\n{characteristic}\n")

    def create(self, validated_data: dict):
        print(f">>>\n{validated_data}\n")

        valid_group = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")

        # animal
        new_group, _ = Group.objects.get_or_create(**valid_group)

        animal = Animal.objects.create(**validated_data, group=new_group)

        for item in characteristics:
            # criar na tabela de characteristic
            new_characteristic, _ = Characteristic.objects.get_or_create(**item)
            animal.characteristics.add(new_characteristic)

        return animal
        # characteristic = Characteristic.objects.create(**validated_data)
        # animal = Animal.objects.create(**validated_data)

    # Separar informações que estão vindo da sua requisição para preencher as respectivas models (Animal, Group e Characteristic)

    # Verificar se o group existe, caso não exista você deve criar

    # Utilização do método get_or_create, para fazer a verificação se existe ou não ou se cria ou não, na parte de Group e Characteristics https://docs.djangoproject.com/en/4.0/ref/models/querysets/ da um ctrl f e procura por get_or_create

    # Instanciar Animal com suas informações atrelando o group criado

    # O mesmo processo de para group, lembrando que characteristics é uma lista de characteristic
