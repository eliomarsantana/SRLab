# -*- coding: utf 8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from models import Localizacao, Aula, TipoUso, Laboratorio, PacoteDeSoftware, Software, Computadores, Reserva, Reserva_Uso_Lab, Reserva_Estado_Uso_Lab

admin.site.register(Localizacao)
admin.site.register(Aula)
admin.site.register(TipoUso)
admin.site.register(Laboratorio)
admin.site.register(PacoteDeSoftware)
admin.site.register(Software)
admin.site.register(Computadores)
admin.site.register(Reserva)
admin.site.register(Reserva_Uso_Lab)
admin.site.register(Reserva_Estado_Uso_Lab)
