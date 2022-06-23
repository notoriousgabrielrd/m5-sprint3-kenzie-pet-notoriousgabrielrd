from django.db import models
from django.forms import CharField

# Create your models here.


class Characteristic(models.Model):
    name = models.CharField(unique=True, max_length=20)
