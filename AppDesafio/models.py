from django.db import models
# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=35)
    apellido=models.CharField(max_length=35)
    DNI=models.IntegerField()
    fecha_nacimiento=models.DateField()
