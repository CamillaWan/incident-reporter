from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from .forms import IncidentForm


def incident_list(request):
    limit = 5
    incidents = Incident.objects.all()[:limit]  # Fetch the first 5 incidents
    total_count = Incident.objects.count()
    has_more = total_count > limit
    next_offset = limit

    form = IncidentForm()
    return render(request, 'reporter/list.html', {
        'incidents': incidents, 
        'form': form,
        'has_more': has_more,
        'next_offset': next_offset,
    })

def load_more_incidents(request):
    offset = int(request.GET.get('offset', 0))
    limit = 5
    queryset = Incident.objects.order_by('-timestamp')
    total_count = queryset.count()
    incidents = queryset[offset:offset + limit]
    has_more = (offset + limit) < total_count

    return render(request, 'reporter/partials/incident_rows.html', {
        'incidents': incidents,
        'has_more': has_more,
        'next_offset': offset + limit,
    })

def add_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            limit = 5
            incidents = Incident.objects.all()[:limit]
            total_count = Incident.objects.count()
            has_more = total_count > limit
            next_offset = limit

            return render(request, 'reporter/partials/incident_table.html', {
                'incidents': incidents,
                'has_more': has_more,
                'next_offset': next_offset,
            })
    return HttpResponse(status=400)
