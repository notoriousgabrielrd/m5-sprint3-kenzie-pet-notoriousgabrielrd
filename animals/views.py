from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from animals.serializer import AnimalSerializer
from .models import Animal

# Create your views here.


class AnimalView(APIView):
    def post(self, request):

        # serializer = AnimalSerializer(data=request.data)

        serializer = AnimalSerializer(data=request.data)
        print(serializer)

        serializer.is_valid(raise_exception=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        animal = serializer.save()
        print(f">>>animal: \n{animal}\n")

        # serializer = AnimalSerializer(animal)
        # print(f">>>serializer: \n{serializer}\n")

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):

        # users = User.objects.all()

        # serializer = UserSerializer(users, many=True)

        # return Response(serializer.data)

        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)


class AnimalViewDetail(APIView):
    def get(self, request, animal_id):

        try:
            # animal = get_object_or_404(Animal, pk=animal_id)
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found."}, status.HTTP_404_NOT_FOUND)

        serializer = AnimalSerializer(animal)

        return Response(serializer.data)

    def patch(self, request, animal_id):

        try:
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found."}, status.HTTP_404_NOT_FOUND)
        print(animal)
        serializer = AnimalSerializer(animal, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            print("chegou aqui")
        except KeyError:
            # print(f">>>\n{request.data}\n")

            for key, value in request.data.items():
                if key == "sex" or key == "group" or key == "characteristics":
                    return Response(
                        {"error": f"You can't update {key} property!"},
                        status.HTTP_422_UNPROCESSABLE_ENTITY,
                    )

        return Response(serializer.data)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
