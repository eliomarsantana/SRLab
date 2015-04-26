from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, loader
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

# Create your views here.

def AppRelatorios(request):
    return render_to_response("SRLab/index_relatorios.html")

def ReservaNaoAtendida(request):
    ReservaNaoAtendida = PrioridadeDeReserva.objects.filter(Reserva_Atendida=False)
    return render_to_response("SRLab/ReservaNaoAtendida.html")

