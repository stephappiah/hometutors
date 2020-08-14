from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile, UserType
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)
@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user', 'fname', 'lname', 'location', 'address', 'teach_levels', 'tutoring_programs',
     'courses_subjects', 'highest_education', 'class_type', 'bio', )

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type',)