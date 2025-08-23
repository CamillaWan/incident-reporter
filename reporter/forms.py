from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'severity', 'location', 'resident', 'description', 'reporter']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }