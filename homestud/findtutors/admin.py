from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile, UserType, Education, TutorProfile
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'highest_education', 'class_type', 'bio')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'programme', 'start_year', 'end_year')

@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'location', 'address')

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')