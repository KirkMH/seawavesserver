from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.site_header = 'Sea-condition Emergency Alert and Warning Apparatus for Vessel Safety'
admin.site.site_title  =  'SEAWAVES Server'
admin.site.index_title  =  'System Administrator'


class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'owner_contact', 'length', 'width', 'height', 'registered_at', 'is_active')
admin.site.register(Boat, BoatAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('boat', 'heading_angle', 'pitch_angle', 'roll_angle', 'latitude', 'longitude', 'altitude', 'timestamp')
admin.site.register(Record, RecordAdmin)

class SettingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'critical_pitch_angle', 'critical_roll_angle', 'reading_rate', 'saving_rate', 'sms_rate', 'post_rate', 'mobile_number')
admin.site.register(Setting, SettingAdmin)

class BulletinAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'available_until', 'created_at', 'created_by')
admin.site.register(Bulletin, BulletinAdmin)

admin.site.unregister(Group)