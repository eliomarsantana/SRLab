from django import forms
from Administrativo.models import Reserva
from Administrativo.models import PacoteDeSoftware, Aula, Laboratorio, UsoInternet

class FormReserva(forms.ModelForm):
    Data_da_Reserva = forms.DateField(
                    widget=forms.DateInput(format='%d/%m/%Y'),
                    input_formats=['%d/%m/%Y', '%d/%m/%y'])
    Tipo_Aula = Aula.objects.all()
    Laboratorio = Laboratorio.objects.all()
    Pacotes = PacoteDeSoftware.objects.all()
    UsoInternet = UsoInternet.objects.all()
    class Meta:
        model = Reserva