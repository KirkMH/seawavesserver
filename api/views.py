from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from monitoring.models import Boat, Record, Setting
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
    serializer = RecordSerializer(data=request.data)
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
    count = 50
    qpBoat = request.query_params.get('boat')

    # qpCount = request.query_params.get('count')
    # if qpCount != None:
    #     count = int(qpCount)
    boat = Boat.objects.get(pk=qpBoat)
    records = Record.objects.filter(boat=qpBoat).order_by('-pk')[:count]
    ordered = records.order_by('timestamp')
    
    serializer = RecordSerializer(ordered, many=True)
    return Response(serializer.data)