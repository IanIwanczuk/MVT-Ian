from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=16)
    apellido = models.CharField(max_length=16)
    nacimiento = models.CharField(max_length=16)
    edad = models.IntegerField()