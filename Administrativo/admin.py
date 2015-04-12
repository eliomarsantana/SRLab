# -*- coding: utf 8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from models import Localizacao, Aula, TipoUso, Laboratorio, PacoteDeSoftware, Software, Computadores

class LaboratorioAdmin(admin.ModelAdmin):
    search_fields = ['Numero_de_Maquinas']

class ReservaAdmin(admin.ModelAdmin):
    search_fields = ['Numero_de_Maquinas']
   
admin.site.register(Localizacao)
admin.site.register(Aula)
admin.site.register(TipoUso)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(PacoteDeSoftware)
admin.site.register(Software)
admin.site.register(Computadores)