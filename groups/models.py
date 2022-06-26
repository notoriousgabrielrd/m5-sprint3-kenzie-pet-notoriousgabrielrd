from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(unique=True, max_length=20)
    scientific_name = models.CharField(unique=True, max_length=50)
