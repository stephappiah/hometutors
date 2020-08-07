# from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from .multi_choices import shs_choices, teach_level_choices, free_lesson_choices, highest_education_choices, class_type_choices, user_type_choices, primary_choices, jhs_choices
from .courses import shs_courses_choices

#User Profile
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    contact = PhoneNumberField(null=True, blank=True, region='GH')

class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=user_type_choices, null=True, blank=True)

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    programme = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.DateField(null=True, blank=True)
    end_year = models.DateField(null=True, blank=True)


class TutorProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    highest_education = models.CharField(max_length=20, choices=highest_education_choices, null=True, blank=True)
    class_type = MultiSelectField(choices=class_type_choices, null=True, blank=True)
    free_lesson_duration = models.IntegerField(choices=free_lesson_choices, null=True, blank=True)
    rate_per_hour = models.IntegerField(null=True, blank=True)

    
class TutorInterest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    teach_levels = MultiSelectField(choices=teach_level_choices, null=True, blank=True)
    primary_programs = MultiSelectField(choices=primary_choices, null=True, blank=True)
    jhs_programs = MultiSelectField(choices=jhs_choices, null=True, blank=True)
    shs_programs = models.CharField(max_length=20, choices=shs_choices, null=True, blank=True)
    shs_courses = MultiSelectField(choices=shs_courses_choices, null=True, blank=True)
        
