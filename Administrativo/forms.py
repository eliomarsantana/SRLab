from django import forms
from models import SoftwareReservaLab, Reserva, Software

class FormSoftwareReserva(forms.ModelForm):
    reserva = Reserva.objects.all()
    software = Software.objects.all()
    class Meta:
        model = SoftwareReservaLab