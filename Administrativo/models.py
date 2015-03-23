from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    Nivel = models.IntegerField()
    Predio = models.CharField(max_length=60)
    Numero_de_Maquinas = models.IntegerField()
    Lotacao_Maxima = models.IntegerField()
    Tipo_DeUso = models.ForeignKey('TipoDeUso')

class TipoDeUso(models.Model):
    tipo_de_uso = models.CharField(max_length=30)


class Computadores(models.Model):
    Quantidad_de_Memoria = models.IntegerField()
    Frequencia_do_Processador = models.CharField(max_length=20)
    Presenca_de_CD_Disquete = models.CharField(max_length=20)

class Software(models.Model):
    nome = models.CharField(max_length=60)
    versao = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)

class TipoAula(models.Model):
    descricao = models.CharField(max_length=100)

class Reserva(models.Model):
    loginUsuario = models.CharField(max_length=60)
    UsoDoLaboratorio = models.BinaryField()
    EstadoFuncional = models.BinaryField()