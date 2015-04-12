# -*- coding: utf 8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('INFORÇÕES DA RESERVA', {'fields': ['Data_da_Reserva'], 'classes':['collapse']}),
        ('INFORMAÇÕES DO LABORATÓRIO', {'fields': ['Laboratorio', 'Tipo_Aula'], 'classes':['collapse']}),
        ('INFORÇÕES DE REQUISITOS DE SOFTWARE', {'fields': ['Uso_Internet', 'Pacotes'], 'classes':['collapse']}),
    ]

admin.site.register(Reserva, ReservaAdmin)