from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from .forms import IncidentForm
from django.core.paginator import Paginator


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
    page_number = int(request.GET.get('page', 1))
    limit = 5
    incidents = Incident.objects.all()
    paginator = Paginator(incidents, limit)
    page_obj = paginator.get_page(page_number)

    has_next = page_obj.has_next()
    next_page = page_obj.next_page_number() if has_next else None

    return render(request, 'reporter/partials/incident_rows.html', {
        'incidents': page_obj.object_list,
        'has_next': has_next,
        'next_page': next_page,
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
