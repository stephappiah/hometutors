from django.contrib import admin
from .models import GroupClass
from django.contrib.gis.admin import OSMGeoAdmin

@admin.register(GroupClass) 
class GroupClassAdmin(OSMGeoAdmin):
    list_display = ('tutor', 'subjects', 'programs', 'address')
    