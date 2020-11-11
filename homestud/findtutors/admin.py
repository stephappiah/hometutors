from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import TutorProfile
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)
@admin.register(TutorProfile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'fullname', 'location', 'address', 'teach_levels', 'tutoring_programs',
     'courses_subjects', 'highest_education', 'class_type', 'bio', 'slug')