from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'severity', 'location', 'incident_date_time', 'resident', 'description', 'actions_taken', 'reporter', 'reported_to_manager']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder':'describe what happened...', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., Room 101, Lobby', 'class': 'form-control'}),
            'incident_date_time': forms.DateTimeInput(
            attrs={
                'type': 'datetime-local', # HTML5 datetime-local input
                'class': 'form-control', # Bootstrap class for styling
            }, format='%Y-%m-%dT%H:%M'), # Format for datetime-local input
            'resident': forms.TextInput(attrs={'placeholder': 'resident name e.g., John Doe', 'class': 'form-control'}),
            'reporter': forms.TextInput(attrs={'placeholder': 'staff name e.g., Jane Smith', 'class': 'form-control'}),
            'actions_taken': forms.Textarea(attrs={'rows': 2, 'placeholder':'describe any actions taken...', 'class': 'form-control'}), 
        }