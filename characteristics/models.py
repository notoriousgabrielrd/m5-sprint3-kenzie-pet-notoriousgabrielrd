from django.db import models

# from animals.models import Animal


# from groups.models import Group

# Create your models here.


class Characteristic(models.Model):
    name = models.CharField(unique=True, max_length=20)

    # groups = models.ManyToManyField(Group, related_name="groups")

    # animals = models.ManyToManyField(Animal, related_name="animals")
