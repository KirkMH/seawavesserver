from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.site_header = 'Sea-condition Emergency Alert and Warning Apparatus for Vessel Safety'
admin.site.site_title  =  'SEAWAVES Server'
admin.site.index_title  =  'System Administrator'


# custom action for admin to perform stock adjustment
@admin.action(description='Deactivate selected boats')
def deactivate_boats(modeladmin, request, queryset):
    for req in queryset:
        req.is_active = False
        req.save()
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'owner_contact', 'length', 'width', 'height', 'registered_at', 'is_active')
    actions = [deactivate_boats]
admin.site.register(Boat, BoatAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('boat', 'voyage', 'heading_angle', 'pitch_angle', 'roll_angle', 'latitude', 'longitude', 'altitude', 'signalStrength', 'timestamp')
admin.site.register(Record, RecordAdmin)

class SettingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'critical_pitch_angle', 'critical_roll_angle', 'reading_rate', 'saving_rate', 'sms_rate', 'post_rate', 'mobile_number')
admin.site.register(Setting, SettingAdmin)

class BulletinAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'available_until', 'created_at', 'created_by')
admin.site.register(Bulletin, BulletinAdmin)

class VoyageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'boat', 'started_at', 'ended_at', 'max_roll', 'max_pitch', 'max_speed', 'avg_speed')
admin.site.register(Voyage, VoyageAdmin)

class LocalReadingAndErrorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'boat', 'recorded_on')
admin.site.register(LocalReadingAndError, LocalReadingAndErrorAdmin)

class FocusBoatAdmin(admin.ModelAdmin):
    list_display = ('pk', 'boat', )
admin.site.register(FocusBoat, FocusBoatAdmin)

admin.site.unregister(Group)