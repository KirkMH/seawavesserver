from django.shortcuts import render
from monitoring.models import Boat

def route_view(request):
    context = {
        'boats': Boat.objects.all().order_by('name'),
    }
    return render(request, 'reporting/route.html', context)