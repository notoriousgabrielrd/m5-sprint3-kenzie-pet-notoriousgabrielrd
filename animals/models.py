from django.db import models

# from characteristics.models import Characteristic

from groups.models import Group

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="animals")

    # Characteristic = models.ManyToManyField
    characteristics = models.ManyToManyField(
        "characteristics.Characteristic", related_name="animals"
    )
