from django.contrib import admin
from Administrativo.models import Laboratorio, Computadores, Software, TipoAula, Reserva, TipoDeUso


admin.site.register(TipoDeUso)
admin.site.register(Laboratorio)
admin.site.register(Computadores)
admin.site.register(Software)
admin.site.register(TipoAula)
admin.site.register(Reserva)

