from django.shortcuts import render
from django.http import HttpResponse
from  django.template.loader import get_template
from  django.template import Context, loader
from Administrativo.models import Laboratorio

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.core.context_processors import request

from forms import FormReserva
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from Usuario.models import Reserva
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
            item.save()
            return HttpResponseRedirect("/Usuario")
    else:
        form = FormReserva()

    return render_to_response("SRLab/cadastro.html", {'form': form},
            context_instance=RequestContext(request))

@login_required(login_url='/Usuario/Login/')
def consultar(request):
    #return render(request,'SRLab/index_usuario_consultar.html')
    reservas = Reserva.objects.all()
    return render_to_response("SRLab/consultarResultado.html", {'reserva': reservas})

class ConsultarUsuario(TemplateView):
    def post(self, request, *args, **kwargs):
       # buscar = request.POST['consultarSoftLab']
        reservas = Reserva.objects.all()
        for reserva in reservas:
            print reserva.Laboratorio
        return render(request, "SRLab/index_usuario_consultar_resultado.html",
                                {'reservas': reservas, 'reserva': True})
