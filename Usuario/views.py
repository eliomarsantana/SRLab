from django.shortcuts import render
from django.http import HttpResponse
from  django.template.loader import get_template
from  django.template import Context, loader
from Administrativo.models import Laboratorio

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.core.context_processors import request

from forms import FormReserva
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from Administrativo.models import PacoteLaboratorio, PrioridadeDeReserva,Reserva
from django.views.generic import TemplateView
from Administrativo.forms import FormSoftwareReserva

import datetime
# Create your views here.

@login_required(login_url='/Usuario/Login/')
def index(request):
    name = 'teste'
    t = loader.get_template('SRLab/index_usuario.html')
    c = Context({'usuarios': name})
    return HttpResponse(t.render((c)))

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect("/Usuario")
        else:
            return render(request, "SRLab/index.html", {"form": form})
    
    return render(request, "SRLab/logar.html", {"form": AuthenticationForm()})

@login_required(login_url='/Usuario/Login/')
def cadastrar(request):
    if request.method == 'POST':
        form = FormReserva(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            print request.POST['Laboratorio']
            print request.user
            print request.POST['Data_da_Reserva']
            item.save()
            
            return HttpResponseRedirect("/Usuario")
    else:
        form = FormReserva()

    return render_to_response("SRLab/cadastro.html", {'form': form, 'Laboratorios': form.Laboratorio, 'UsoDeInternet':form.UsoInternet, 'TipoAula':form.Tipo_Aula },
            context_instance=RequestContext(request))

def deslogar(request):
    logout(request)
    return index(request)

@login_required(login_url='/Usuario/Login/')
def consultar(request):
    return render(request,"SRLab/index_usuario_consultar.html")

def RelacaoPacoteSoftInstaladoLaboratorio(request):
    PacotesSoftInstalados = PacoteLaboratorio.objects.all()
    return render_to_response('SRLab/consultarResultado.html',{'resultado': PacotesSoftInstalados})


def PrazoAtenReservaLaboratorio(request):
    LaboratorioReserva = PrioridadeDeReserva.objects.all()
    return render_to_response('SRLab/prazoSolicitacaoReservaLab.html', {'resultadoLaboratorio': LaboratorioReserva})

def LaboratorioReserData(request):
    data = request.POST['data']
    LabReserva = Reserva.objects.filter(Data_da_Reserva = datetime.date(int(data[6:10]),int(data[3:5]),int(data[0:2])))
    return render_to_response('SRLab/consultarLabPorData.html', {'Laboratorio': LabReserva})

@login_required(login_url='/Usuario/Login/')
def solicitarReserva(request):
    if request.method == 'POST':
        form = FormSoftwareReserva(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()

            return HttpResponseRedirect("/Usuario")
    else:
        form = FormSoftwareReserva()

    return render_to_response("SRLab/solicitacaoSoftware.html", {'form': form},
            context_instance=RequestContext(request))
