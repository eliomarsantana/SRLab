from django.db import models

# Create your models here.
class Niveis(models.Model):
    nivel = models.CharField(max_length=60)

    def __str__(self):
        return self.nivel


class Locais(models.Model):
    Local = models.CharField(max_length=60)
    nivel = models.ForeignKey('Niveis')

    def __str__(self):
        return self.Local

class Laboratorio(models.Model):
    Predio = models.CharField(max_length=60)
    Numero_de_Maquinas = models.IntegerField()
    Lotacao_Maxima = models.IntegerField()
    Tipo_De_Uso = models.ForeignKey('TipoLaboratorio')
    Locais = models.ForeignKey('Locais')

class TipoLaboratorio(models.Model):
    tipo_de_uso = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_de_uso

class Computadores(models.Model):
    Quantidad_de_Memoria = models.IntegerField()
    Frequencia_do_Processador = models.CharField(max_length=20)
    Presenca_de_CD_Disquete = models.CharField(max_length=20)

class Software(models.Model):
    nome = models.CharField(max_length=60)
    versao = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    Pacote = models.ForeignKey('PacoteDeSoftware')

class PacoteDeSoftware(models.Model):
    pacote = models.CharField(max_length=60)

    def __str__(self):
        return self.pacote

class TipoAula(models.Model):
    descricao = models.CharField(max_length=100)

class Reserva(models.Model):
    loginUsuario = models.CharField(max_length=60)
    UsoDoLaboratorio = models.ForeignKey('Reserva_Uso_Lab')
    EstadoFuncional = models.ForeignKey('Reserva_Estado_Uso_Lab')
    Data_da_Reserva = models.DateTimeField()

class Reserva_Uso_Lab(models.Model):
    uso = models.CharField(max_length=10)

    def __str__(self):
        return self.uso

class Reserva_Estado_Uso_Lab(models.Model):
    situacao = models.CharField(max_length=10)

    def __str__(self):
        return self.situacao