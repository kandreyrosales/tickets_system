from django import forms
from apps.tickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'description',
        ]
        labels = {
            'description':'Description',
        }

        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'response'
        ]
        labels = {
            'response': 'Response'
        }