from django import forms
from ticket.models import Ticket

class TicketSubmit(forms.Form):
    title = forms.CharField(max_length=50)
    bug = forms.CharField(widget=forms.Textarea)