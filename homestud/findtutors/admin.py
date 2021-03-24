from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TutorProfile, TutorReview
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)
admin.site.register(TutorReview)

@admin.register(TutorProfile) 
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'first_name', 'address', 'highest_education', 'slug', 'admin_show', 'show_profile')