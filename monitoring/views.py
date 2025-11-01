from django.shortcuts import render, get_object_or_404, redirect
from django_serverside_datatable.views import ServerSideDatatableView
from .models import Bulletin, Setting, Boat, Record, Voyage, FocusBoat
from .forms import BoatForm, SettingForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    adopter = request.user.userprofile.adopter
    hour = datetime.now().hour
    greeting = 'Good {}!'.format(
        'morning' if hour < 12 else 'afternoon' if hour < 18 else 'evening')
    boat_count = Boat.objects.filter(adopter=adopter, is_active=True).count()

    context = {
        'bulletin_list': Bulletin.available.filter(adopter=adopter),
        'greeting': greeting,
        'setting': Setting.objects.filter(adopter=adopter).last(),
        'boat_count': boat_count
    } 
    return render(request, 'dashboard.html', context)


@login_required
def boat_listview(request):
    return render(request, 'monitoring/boat_list.html')

class BoatDTListView(ServerSideDatatableView):

    def get(self, request, *args, **kwargs):
        adopter = request.user.userprofile.adopter
        self.queryset = Boat.objects.filter(adopter=adopter)
        self.columns = ['pk', 'name', 'owner', 'owner_contact', 'length', 'width', 'height', 'registered_at', 'is_active']
        return super().get(request, *args, **kwargs)
    
    
    
@login_required
def voyage_listview(request, pk):
    request.session['boat_id'] = pk
    adopter = request.user.userprofile.adopter
    setting = Setting.objects.filter(adopter=adopter).last()
    context = {
        'boat': Boat.objects.get(pk=pk),
        'post_interval': setting.post_rate
    }
    return render(request, 'monitoring/boat_voyage.html', context)

class VoyageDTListView(ServerSideDatatableView):
	
    def get(self, request, *args, **kwargs):
        pk = request.session.get('boat_id', 0)
        boat = get_object_or_404(Boat, pk=pk)
        self.queryset = Voyage.objects.filter(boat=boat)
        self.columns = ['pk', 'started_at', 'ended_at', 'max_roll', 'max_pitch', 
                        'max_speed', 'avg_speed']
        return super().get(request, *args, **kwargs)
    
    
@login_required
def record_listview(request, pk):
    request.session['voyage_id'] = pk
    voyage = Voyage.objects.get(pk=pk)
    adopter = request.user.userprofile.adopter
    setting = Setting.objects.filter(adopter=adopter).last()
    context = {
        'boat': voyage.boat,
        'voyage': voyage,
        'post_interval': setting.post_rate
    }
    return render(request, 'monitoring/boat_record.html', context)

class RecordDTListView(ServerSideDatatableView):
	
    def get(self, request, *args, **kwargs):
        pk = request.session.get('voyage_id', 0)
        voyage = get_object_or_404(Voyage, pk=pk)
        self.queryset = Record.objects.filter(voyage=voyage)
        self.columns = ['pk', 'timestamp', 'latitude', 'longitude', 'altitude', 
                        'heading_angle', 'pitch_angle', 'roll_angle', 
                        'gyro_x', 'gyro_y', 'gyro_z', 
                        'accel_x', 'accel_y', 'accel_z', 
                        'mag_x', 'mag_y', 'mag_z', 'signalStrength', 'speed', 'sent_timestamp']
        return super().get(request, *args, **kwargs)

class FocusRecordDTListView(ServerSideDatatableView):
	
    def get(self, request, *args, **kwargs):
        pk = 0
        fboat = FocusBoat.objects.filter(adopter=request.user.userprofile.adopter).last()
        if fboat:
            boat_voyage = Voyage.objects.filter(boat=fboat.boat).last()
            if boat_voyage:
                pk = boat_voyage.pk
        voyage = get_object_or_404(Voyage, pk=pk)
        self.queryset = Record.objects.filter(voyage=voyage)
        self.columns = ['pk', 'timestamp', 'latitude', 'longitude', 'altitude', 
                        'heading_angle', 'pitch_angle', 'roll_angle', 
                        'gyro_x', 'gyro_y', 'gyro_z', 
                        'accel_x', 'accel_y', 'accel_z', 
                        'mag_x', 'mag_y', 'mag_z', 'signalStrength', 'speed', 'sent_timestamp']
        return super().get(request, *args, **kwargs)

def instructions_view(request):
    return render(request, 'monitoring/api_instructions.html')

@login_required
def map_view(request):
    adopter = request.user.userprofile.adopter
    print(f"adopter: {adopter}")
    fboat = FocusBoat.objects.filter(adopter=adopter).last()
    voyage_pk = 0
    if fboat:
        voyage = Voyage.objects.filter(boat=fboat.boat).last()
        if voyage:
            voyage_pk = voyage.pk
    boats = Boat.objects.filter(is_active=True, adopter=adopter)
    print(f"boats: {boats}")
    boats = [boat for boat in boats if boat.is_still_navigating]
    print(f"filtered boats: {boats}")
    boat_count = 0
    y_count = 0
    o_count = 0
    r_count = 0
    for b in boats:
        boat_count += 1
        c = b.get_color()
        if c == 'yellow':
            y_count += 1
        elif c == 'orange':
            o_count += 1
        elif c == 'red':
            r_count += 1

    context = {
        'setting': Setting.objects.filter(adopter=adopter).last(),
        'adopter': adopter,
        'boat_count': boat_count,
        'y_count': y_count, 
        'o_count': o_count, 
        'r_count': r_count,
        'focus': fboat,
        'voyage_pk': voyage_pk
    } 
    return render(request, 'map.html', context)


@login_required
def update_boat(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    form = BoatForm(instance=boat)
    status = ""

    if request.method == 'POST':
        form = BoatForm(request.POST, instance=boat)
        if form.is_valid():
            form.save()
            status = "success"

    return render(request, 'monitoring/update_boat.html', {'boat': boat, 'form': form, 'status': status})


@login_required
def update_settings(request):
    setting = Setting.objects.filter(adopter=request.user.userprofile.adopter).last()
    form = SettingForm(instance=setting)
    status = ""

    if request.method == 'POST':
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            status = "success"
    
    print(f'status: {status}')
    return render(request, 'monitoring/update_settings.html', {'setting': setting, 'form': form, 'status': status})