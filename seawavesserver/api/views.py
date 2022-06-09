from rest_framework.response import Response
from rest_framework.decorators import api_view
from monitoring.models import Boat, Record, Setting
from .serializers import BoatSerializer, RecordSerializer, SettingSerializer


@api_view(['GET'])
def getBoats(request):
    '''
    Returns the record of all registered boats.
    '''
    boats = Boat.objects.all()
    serializer = BoatSerializer(boats, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBoat(request):
    '''
    Registers the boat into the system.
    '''
    serializer = BoatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
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
    records = Record.objects.all()
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
    return Response(serializer.data)