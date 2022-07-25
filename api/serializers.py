from rest_framework import serializers
from monitoring.models import Boat, Record, Setting

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

class BoatLocationSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField('getLatitude')
    longitude = serializers.SerializerMethodField('getLongitude')
    color = serializers.SerializerMethodField('getColor')
    heading = serializers.SerializerMethodField('getHeading')
    pitch = serializers.SerializerMethodField('getPitch')
    roll = serializers.SerializerMethodField('getRoll')

    def getLatitude(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.latitude if rec != None else None

    def getLongitude(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.longitude if rec != None else None

    def getColor(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.getColor() if rec != None else None

    def getHeading(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.heading_angle if rec != None else None

    def getPitch(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.pitch_angle if rec != None else None
        
    def getRoll(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.roll_angle if rec != None else None

    class Meta:
        model = Boat
        fields = ('id', 'name', 'latitude', 'longitude', 'color', 'heading', 'pitch', 'roll')