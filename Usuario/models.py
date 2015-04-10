from django.db import models
from Administrativo.models import Aula, Laboratorio, PacoteDeSoftware
# Create your models here.
class Reserva(models.Model):
    Data_da_Reserva = models.DateTimeField()
    Tipo_Aula = models.ForeignKey(Aula)
    Laboratorio = models.OneToOneField(Laboratorio)
    Uso_Internet = models.CharField(max_length=1)
    Pacotes = models.ManyToManyField(PacoteDeSoftware)