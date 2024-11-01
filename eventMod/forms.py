from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'start_date', 'end_date', 'description']



