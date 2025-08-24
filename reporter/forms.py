from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'severity', 'location', 'incident_date_time', 'resident', 'description', 'reporter']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., Room 101, Lobby', 'class': 'form-control'}),
            'incident_date_time': forms.DateTimeInput(
            attrs={
                'type': 'datetime-local', # HTML5 datetime-local input
                'class': 'form-control', # Bootstrap class for styling
            }, format='%Y-%m-%dT%H:%M'),
        }