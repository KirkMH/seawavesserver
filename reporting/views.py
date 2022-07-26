from django.shortcuts import render
from monitoring.models import Boat

def route_view(request):
    context = {
        'boats': Boat.objects.all(),

    }
    return render(request, 'reporting/route.html', context)