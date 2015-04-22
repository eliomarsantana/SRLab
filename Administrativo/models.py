from django.db import models
# Create your models here.
class Localizacao(models.Model):
    nivel = models.CharField(max_length=60)
    Predio = models.CharField(max_length=60)
    def __str__(self):
        return "Nivel "+self.nivel+" - "+self.Predio

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

    def __str__(self):
        return self.Locais.__str__()

class Reserva(models.Model):
    Data_da_Reserva = models.DateTimeField()
    Tipo_Aula = models.ForeignKey('Aula')
    Laboratorio = models.ForeignKey('Laboratorio')
    Uso_Internet = models.CharField(max_length=1)
    def __str__(self):
        return "Lab.: "+self.Laboratorio.__str__()+" - Tipo de aula: "+self.Tipo_Aula.__str__()

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

class PacoteLaboratorio(models.Model):
    Pacotes = models.ForeignKey('PacoteDeSoftware')
    Laboratorio = models.ForeignKey('Laboratorio')
    Data_Solicitacao = models.DateField()
    Hora_Solicitacao = models.TimeField()

class EstadoLaboratorio(models.Model):
    Estado_Laboratorio = models.CharField(max_length=20)
    def __str__(self):
        return self.Estado_Laboratorio

class UsoLaboratorio(models.Model):
    Uso = models.TextField(max_length=20)
    def __str__(self):
        return self.Uso
class NivelPrioridadeReserva(models.Model):
    Nivel = models.TextField(max_length=1)
    def __str__(self):
        return self.Nivel
class AtedimentoReserva(models.Model):
    Atendida = models.TextField(max_length=5)
    def __str__(self):
        return self.Atendida

class EstadoLaboratorioReserva(models.Model):
    Laboratorio = models.ForeignKey('Laboratorio')
    Estado_Laboratorio = models.ForeignKey('EstadoLaboratorio')
    Laboratorio_Reserva = models.ForeignKey(Reserva)
    Uso_Laboratorio = models.ForeignKey('UsoLaboratorio')
    def __str__(self):
        return self.Laboratorio.__str__()

class PrioridadeDeReserva(models.Model):
    Reserva = models.ForeignKey('Reserva')
    Data_Autorizacao = models.DateField()
    Data_Atendimento_da_Reserva = models.DateField()
    Hora_Autorizacao = models.TimeField()
    Prioridade = models.ForeignKey('NivelPrioridadeReserva')
    Reserva_Atendida = models.ForeignKey('AtedimentoReserva')
    def __str__(self):
        return "Data da autorizacao"+self.Data_Autorizacao

