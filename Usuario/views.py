from django.shortcuts import render
from django.http import HttpResponse
from  django.template.loader import get_template
from  django.template import Context, loader

# Create your views here.

def index(request):
    name = 'teste'
    t = loader.get_template('SRLab/index_usuario.html')
    c = Context({'usuarios': name})
    return HttpResponse(t.render((c)))

