# -*- coding: utf 8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from models import Laboratorio, Computadores, Software, TipoAula, Reserva, TipoLaboratorio, Locais, Niveis, PacoteDeSoftware, Reserva_Uso_Lab , Reserva_Estado_Uso_Lab

class LaboratorioAdministrador(admin.ModelAdmin):
    fieldsets = [
        ('CAPACIDADE', {'fields': ['Numero_de_Maquinas', 'Lotacao_Maxima'], 'classes':['collapse']}),
        ('LOCALIZAÇÃO', {'fields': ['Predio', 'Locais'], 'classes':['collapse']}),
        ('UTILIZAÇÃO', {'fields': ['Tipo_De_Uso'],'classes':['collapse']}),
    ]

class CoputadoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ('MEMÓRIA', {'fields': ['Quantidad_de_Memoria'],'classes':['collapse']}),
        ('PROCESSADOR', {'fields': ['Frequencia_do_Processador'],'classes':['collapse']}),
        ('ARMAZENAMENTO', {'fields': ['Presenca_de_CD_Disquete'],'classes':['collapse']}),
    ]
class SoftwareAdmin(admin.ModelAdmin):
    fieldsets = [
        ('INFORMAÇÃO GERAIS', {'fields':['nome', 'versao', 'descricao'],'classes':['collapse']}),
        ('EXTENSÃO', {'fields':['Pacote'],'classes':['collapse']}),
    ]
class ReservaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('INFORMAÇÃO DO USUÁRIO', {'fields': ['loginUsuario'], 'classes':['collapse']}),
        ('INFORMAÇÕES DO LABORATÓRIO', {'fields': ['UsoDoLaboratorio', 'EstadoFuncional'], 'classes':['collapse']}),
        ('INFORÇÕES DA RESERVA', {'fields': ['Data_da_Reserva'], 'classes':['collapse']}),
    ]


admin.site.register(Laboratorio, LaboratorioAdministrador)
admin.site.register(Computadores, CoputadoresAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(TipoLaboratorio)
admin.site.register(TipoAula)
admin.site.register(Locais)
admin.site.register(Niveis)
admin.site.register(PacoteDeSoftware)
admin.site.register(Reserva_Uso_Lab)
admin.site.register(Reserva_Estado_Uso_Lab)
