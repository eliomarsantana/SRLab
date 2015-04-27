from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import request
from Administrativo.models import PrioridadeDeReserva


# Create your views here.

def AppRelatorios(request):
    return render_to_response("SRLab/index_relatorios.html")

def ReservaNaoAtendida(request):
    ReservaNaoAtendida = PrioridadeDeReserva.objects.filter(Reserva_Atendida='Nao')
    print ReservaNaoAtendida
    print 'estou aqui'
    return render_to_response('SRLab/ReservaNaoAtendida.html',{'ReservaNaoAtendida': ReservaNaoAtendida})

