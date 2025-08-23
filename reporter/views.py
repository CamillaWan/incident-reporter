from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from .forms import IncidentForm

def incident_list(request):
    incidents = Incident.objects.all()[:5]  # Fetch the first 5 incidents
    form = IncidentForm()
    return render(request, 'reporter/list.html', {'incidents': incidents, 'form': form})

def load_more_incidents(request):
    offset = int(request.GET.get('offset', 0))
    limit = 5
    incidents = Incident.objects.all()[offset:offset+limit]
    return render(request, 'reporter/partials/incident_rows.html', {'incidents': incidents})

def add_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            incidents = Incident.objects.all()[:5]
            return render(request, 'reporter/partials/incident_table.html', {'incidents': incidents})
    return HttpResponse(status=400)
