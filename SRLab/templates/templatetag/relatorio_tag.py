from django import template
from Administrativo.models import PrioridadeDeReserva


#Carrega o registro de template tags
register = template.Library()

#Registra o metodo a seguir como uma inclusion_tag indicando o template a ser renderizad
@register.inclusion_tag('relatorioAdmin.html')
def reservas_n_atendidas():
    reservas = PrioridadeDeReserva.objects.filter(Reserva_Atendida=False)
    print "aqui"
    return { 'reservas' : reservas }
