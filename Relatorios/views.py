from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from Administrativo.models import PrioridadeDeReserva, AtedimentoReserva, EstadoLaboratorioReserva, Reserva


# Create your views here.

@login_required(login_url='/Relatorios/Login/')
def AppRelatorios(request):
    return render_to_response("SRLab/index_relatorios.html")

@login_required(login_url='/Relatorios/Login/')
def ReservaNaoAtendida(request):
    reservas = PrioridadeDeReserva.objects.filter(Reserva_Atendida_id = 1)
    return render_to_response('SRLab/ReservaNaoAtendida.html',{'ReservaNaoAtendida': reservas})

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect("/Relatorios")
        else:
            return render(request, "SRLab/index_relatorio.html", {"form": form})
    
    return HttpResponseRedirect("/admin")    
    #return render(request, "SRLab/logar.html", {"form": AuthenticationForm()})

@login_required(login_url='/Relatorios/Login/')    
def RelatorioEstadoLaboratorioReserva(request):
    reservas = EstadoLaboratorioReserva.objects.all()
    return render_to_response('SRLab/relatorioEstadoLab.html',{'relatorio': reservas})

def ReservaPorProfessor(request):
    ReservaPorProfessor = Reserva.objects.filter(Nome_Usuario = 'professor')
    print ReservaPorProfessor
    return render_to_response('SRLab/consultarReservaPorProfessor.html', {'ReservaPorProfessor': ReservaPorProfessor})
