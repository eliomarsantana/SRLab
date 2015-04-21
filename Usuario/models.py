from django.db import models
from Administrativo.models import Aula, Laboratorio, PacoteDeSoftware
# Create your models here.
class Reserva(models.Model):
    Data_da_Reserva = models.DateTimeField()
    Tipo_Aula = models.ForeignKey(Aula)
    Laboratorio = models.OneToOneField(Laboratorio)
    Uso_Internet = models.CharField(max_length=1)
    Pacotes = models.ManyToManyField(PacoteDeSoftware)
    def __str__(self):
        return "Lab.: "+self.Laboratorio.__str__()+" - Tipo de aula: "+self.Tipo_Aula.__str__()