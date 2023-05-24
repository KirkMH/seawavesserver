from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from monitoring.models import Boat, Record, Setting, Voyage
from .serializers import *
from datetime import datetime


class BoatListView(generics.ListAPIView):
    '''
    Returns the record of all registered boats.
    '''
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

class BoatLocationsListView(generics.ListAPIView):
    '''
    Returns the list of boats with their current location
    '''
    queryset = Boat.objects.filter(is_active=True, record__isnull=False).distinct()
    serializer_class = BoatLocationSerializer

@api_view(['POST'])
def addBoat(request):
    '''
    Registers the boat into the system.
    '''
    serializer = BoatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    response = serializer.data
    return Response(response)
    
@api_view(['GET'])
def getSettings(request):
    '''
    Returns the settings set in the system.
    '''
    settings = Setting.objects.last()
    serializer = SettingSerializer(settings, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getBoatDetail(request):
    '''
    Returns the details of the boat.
    '''
    boatId = request.query_params.get('boatId')
    # retrieve boat's name, owner, and owner's contact and send it as well
    boat = Boat.objects.get(pk=boatId)
    serializer = BoatSerializer(boat, many=False)
    return Response(serializer.data)
    
@api_view(['GET'])
def getRecords(request):
    '''
    Returns all reading records from all boats.
    '''
    qpBoat = request.query_params.get('boat')
    qpFrom = request.query_params.get('from')
    qpTo = request.query_params.get('to')
    records = Record.objects.all()
    if qpBoat != None:
        records = records.filter(boat=qpBoat)
    if qpFrom != None:
        dFrom = datetime.strptime(qpFrom, '%d/%m/%Y').date()
        records = records.filter(timestamp__date__gte=dFrom)
    if qpTo != None:
        dTo = datetime.strptime(qpTo, '%d/%m/%Y').date()
        records = records.filter(timestamp__date__lte=dTo)

    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addRecord(request):
    '''
    Adds a reading from a  boat.
    '''
    print(f"Received data: {request.data}")
    serializer = AddRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(f"Add Record: {serializer.data}")
        return Response(serializer.data)
    else:
        print(f"Add Record error: {serializer.errors}")
        return Response(serializer.errors)

    
@api_view(['GET'])
def getBoatRoute(request):
    '''
    Returns the last 50 records, or the specified number of records,
    of the boat's route.
    '''
    count = 100
    qpBoat = request.query_params.get('boat')

    qpCount = request.query_params.get('count')
    if qpCount != None:
        count = int(qpCount)
    boat = Boat.objects.get(pk=qpBoat)
    records = Record.objects.filter(boat=qpBoat).order_by('-timestamp')[:count]
    
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def startVoyage(request):
    '''
    Starts a voyage by creating a new record in the database and returns its primary key.
    '''
    boatId = request.query_params.get('boatId')
    boat = Boat.objects.get(pk=boatId)
    voyage = Voyage.objects.create(
        boat=boat,
    )
    return Response(voyage.pk)


@api_view(['GET'])
def stopVoyage(request):
    '''
    Ends the voyage by updating the voyage's ended_at field.
    '''
    voyagePk = request.query_params.get('voyagePk')
    voyage = Voyage.objects.get(pk=voyagePk)
    voyage.ended_at = datetime.now()
    voyage.save()
    return Response(voyage.pk)


@api_view(['POST'])
def saveBoatLocalData(request):
    '''
    Saves the boat's local data (readings and errors) into the server database.
    '''
    serializer = AddLocalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    response = serializer.data
    return Response(response)