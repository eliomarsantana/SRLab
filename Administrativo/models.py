from django.db import models

# Create your models here.
class Localizacao(models.Model):
    nivel = models.CharField(max_length=60)
    Predio = models.CharField(max_length=60)
    def __str__(self):
        return self.nivel+"-"+self.Predio

class Aula(models.Model):
    descricao = models.CharField(max_length=100)
    def __unicode(self):
        return self.descricao
    def __str__(self):
        return self.descricao

class TipoUso(models.Model):
    tipo_de_uso = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_de_uso

class Laboratorio(models.Model):
    Numero_de_Maquinas = models.IntegerField()
    Lotacao_Maxima = models.IntegerField()
    Tipo_De_Uso = models.ForeignKey('TipoUso')
    Locais = models.ForeignKey('Localizacao')
    Aula = models.ForeignKey('Aula')

class PacoteDeSoftware(models.Model):
    pacote = models.CharField(max_length=60)

    def __str__(self):
        return self.pacote

class Software(models.Model):
    nome = models.CharField(max_length=60)
    versao = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    Pacote = models.ForeignKey('PacoteDeSoftware')
    
    def __str__(self):
        return self.nome+"-"+self.versao

class Computadores(models.Model):
    Quantidad_de_Memoria = models.IntegerField()
    Frequencia_do_Processador = models.CharField(max_length=20)
    Presenca_de_CD_Disquete = models.CharField(max_length=20)
    Laboratorio = models.ForeignKey('Laboratorio')
    Pacotes = models.ManyToManyField('PacoteDeSoftware')
