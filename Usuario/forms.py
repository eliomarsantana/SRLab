from django import forms
from Administrativo.models import Reserva
from Administrativo.models import PacoteDeSoftware, Aula, Laboratorio, UsoInternet

class FormReserva(forms.ModelForm):
    Nome_Usuario = forms.CharField(max_length=30)
    Email = forms.CharField(max_length=60)
    Horario_Reserva = forms.TimeField()
    """Data_da_Reserva = forms.DateField(
                    widget=forms.DateInput(format='%d/%m/%Y'),
                    input_formats=['%d/%m/%Y', '%d/%m/%y'])"""
    Tipo_Aula = Aula.objects.all()
    Laboratorio = Laboratorio.objects.all()
    Pacotes = PacoteDeSoftware.objects.all()
    UsoInternet = UsoInternet.objects.all()
    class _meta:
        model = Reserva