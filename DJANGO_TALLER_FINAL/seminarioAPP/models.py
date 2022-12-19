from contextlib import nullcontext
from email.policy import default
from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
ESTADOS = [(1,'Reservado'),(2,'Completada'),(3,'Anulada'),(4,'No Asisten')]


class seminario(models.Model):
    id = models.AutoField(primary_key=True)
    nombreR=models.CharField(max_length=50)
    telefono=models.IntegerField()
    institucion=models.CharField(max_length=50)
    fechareserva = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(
        null=False , blank=False,
        choices=ESTADOS,
        default=1

    )
    observacion = models.CharField(max_length=50,
        null=True, blank=True)

class institucion(models.Model):
        id = models.AutoField(primary_key=True)
        nombre=models.CharField(max_length=50)
