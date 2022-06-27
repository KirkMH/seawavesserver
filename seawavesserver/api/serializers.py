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

    def getLatitude(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.latitude

    def getLongitude(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.longitude

    def getColor(self, boat):
        rec = Record.objects.filter(boat=boat).first()
        return rec.getColor()

    class Meta:
        model = Boat
        fields = ('id', 'name', 'latitude', 'longitude', 'color')