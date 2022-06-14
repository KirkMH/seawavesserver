from django.contrib import admin
from .models import *

admin.site.register(Boat)
admin.site.register(Record)
admin.site.register(Setting)
admin.site.register(Bulletin)

# @admin.register(Setting)
# class SettingAdmin(admin.ModelAdmin):
#     # Remove add functionality
#     def has_add_permission(self, request):
#         return False

#     # Remove delete functionality
#     def has_delete_permission(self, request, obj=None):
#         return False