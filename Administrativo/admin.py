from django.contrib import admin
from models import Laboratorio, Computadores, Software, TipoAula, Reserva, TipoLaboratorio, Locais, Niveis, PacoteDeSoftware


admin.site.register(TipoLaboratorio)
admin.site.register(Laboratorio)
admin.site.register(Computadores)
admin.site.register(Software)
admin.site.register(TipoAula)
admin.site.register(Reserva)
admin.site.register(Locais)
admin.site.register(Niveis)
admin.site.register(PacoteDeSoftware)