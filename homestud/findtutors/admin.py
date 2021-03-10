from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TutorProfile, TutorReview
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)
admin.site.register(TutorReview)

@admin.register(TutorProfile) 
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'first_name', 'last_name', 'location', 'address', 'teach_levels', 'tutoring_programs',
     'courses_subjects', 'highest_education', 'class_type', 'bio', 'slug', 'show_profile')