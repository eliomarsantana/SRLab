from django import forms
from models import Reserva
from Administrativo.models import PacoteDeSoftware, Aula, Laboratorio

class FormReserva(forms.ModelForm):
    Data_da_Reserva = forms.DateField(
                    widget=forms.DateInput(format='%d/%m/%Y'),
                    input_formats=['%d/%m/%Y', '%d/%m/%y'])
    Pacotes = PacoteDeSoftware.objects.all()
    Tipo_Aula = Aula.objects.all()
    class Meta:
        model = Reserva
