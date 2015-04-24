# -*- coding: utf 8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from models import Localizacao, Aula, TipoUso, Laboratorio, PacoteDeSoftware, Software, Computadores, EstadoLaboratorio, \
    UsoLaboratorio,NivelPrioridadeReserva,AtedimentoReserva, EstadoLaboratorioReserva, Reserva, PrioridadeDeReserva, PacoteLaboratorio,\
    UsoInternet, SoftwareReservaLab

class LaboratorioAdministrador(admin.ModelAdmin):
    fieldsets = [
        ('CAPACIDADE', {'fields': ['Numero_de_Maquinas', 'Lotacao_Maxima'], 'classes':['collapse']}),
        ('LOCALIZAÇÃO', {'fields': ['Locais'], 'classes':['collapse']}),
        ('UTILIZAÇÃO', {'fields': ['Tipo_De_Uso','Aula'],'classes':['collapse']}),
    ]
class CoputadoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ('MEMÓRIA', {'fields': ['Quantidad_de_Memoria'],'classes':['collapse']}),
        ('PROCESSADOR', {'fields': ['Frequencia_do_Processador'],'classes':['collapse']}),
        ('ARMAZENAMENTO', {'fields': ['Presenca_de_CD_Disquete'],'classes':['collapse']}),
        ('LOCALIZAÇÃO DO EQUIPAMENTO', {'fields': ['Laboratorio'],'classes':['collapse']}),
        ('PACOTES DE SOFTWARES INSTALDOS', {'fields': ['Pacotes'],'classes':['collapse']}),
    ]
class SoftwareAdmin(admin.ModelAdmin):
    fieldsets = [
        ('INFORMAÇÃO GERAIS', {'fields':['nome', 'versao', 'descricao'],'classes':['collapse']}),
        ('PACOTES DE SOFTWARES', {'fields':['Pacote'],'classes':['collapse']}),
    ]
class ReservaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('INFORÇÕES DA RESERVA', {'fields': ['Data_da_Reserva','Horario_Reserva'], 'classes':['collapse']}),
        ('INFORMAÇÕES DO LABORATÓRIO', {'fields': ['Laboratorio', 'Tipo_Aula'], 'classes':['collapse']}),
        ('INFORÇÕES DE REQUISITOS DE SOFTWARE', {'fields': ['Uso_Internet'], 'classes':['collapse']}),
    ]

admin.site.register(Reserva, ReservaAdmin)

admin.site.register(Laboratorio, LaboratorioAdministrador)
admin.site.register(Computadores, CoputadoresAdmin)
admin.site.register(PacoteLaboratorio)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Localizacao)
admin.site.register(Aula)
admin.site.register(TipoUso)
admin.site.register(PacoteDeSoftware)
admin.site.register(EstadoLaboratorio)
admin.site.register(UsoLaboratorio)
admin.site.register(NivelPrioridadeReserva)
admin.site.register(AtedimentoReserva)
admin.site.register(EstadoLaboratorioReserva)
admin.site.register(PrioridadeDeReserva)
admin.site.register(UsoInternet)
admin.site.register(SoftwareReservaLab)