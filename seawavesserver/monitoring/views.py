from django.shortcuts import render
from django_serverside_datatable.views import ServerSideDatatableView
from .models import Bulletin, Setting, Boat
from datetime import datetime


def dashboard_view(request):
    hour = datetime.now().hour
    greeting = 'Good {}!'.format(
        'morning' if hour < 12 else 'afternoon' if hour < 18 else 'evening')
    boat_count = Boat.objects.filter(is_active=True).count()

    context = {
        'bulletin_list': Bulletin.available.all(),
        'greeting': greeting,
        'setting': Setting.objects.last(),
        'boat_count': boat_count
    } 
    return render(request, 'dashboard.html', context)

    
def boat_listview(request):
    return render(request, 'monitoring/boat_list.html')

class BoatDTListView(ServerSideDatatableView):
	queryset = Boat.objects.all()
	columns = ['pk', 'name', 'owner', 'owner_contact', 'length', 'width', 'height', 'registered_at']