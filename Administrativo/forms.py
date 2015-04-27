from django import forms
from models import SoftwareReservaLab, Reserva, Software

class FormSoftwareReserva(forms.ModelForm):
    """Data_da_Solicitacao = forms.DateField(
                    widget=forms.DateInput(format='%d/%m/%Y'),
                    input_formats=['%d/%m/%Y', '%d/%m/%y'])"""
    reserva = Reserva.objects.all()
    software = Software.objects.all()
    class _meta:
        model = SoftwareReservaLab