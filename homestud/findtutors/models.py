# from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from .multi_choices import teach_level_choices, free_lesson_choices, highest_education_choices, class_type_choices, user_type_choices
from .courses import courses_choices, programmes_choices

#User Profile
class TutorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
    dob = models.DateField(null=True, blank=True)
    
    # Education
    school = models.CharField(max_length=100, blank=True, null=True)
    programme = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.DateField(null=True, blank=True)
    end_year = models.DateField(null=True, blank=True)
    # Tutor Profile
    bio = models.CharField(max_length=500, blank=True, null=True)
    highest_education = models.CharField(max_length=20, choices=highest_education_choices, null=True, blank=False)
    class_type = MultiSelectField(choices=class_type_choices, null=True, blank=True)
    free_lesson_duration = models.IntegerField(choices=free_lesson_choices, null=True, blank=True)
    rate_per_hour = models.CharField(max_length=20, null=True, blank=True)
    negotiable = models.BooleanField(default=True, blank=True)
    # Subjects and Programmes
    teach_levels = MultiSelectField(choices=teach_level_choices, null=True, blank=True)
    tutoring_programs = MultiSelectField(choices=programmes_choices, null=True, blank=True)
    courses_subjects = MultiSelectField(choices=courses_choices, null=True, blank=True)

    slug = models.CharField(unique=True, max_length=50, null=True, blank=True)
    show_profile = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_full_name(self):

        if self.first_name != None and self.last_name != None:
            return self.first_name + ' ' + self.last_name
        elif self.first_name == None:
            return self.last_name
        else:
            return self.first_name 

    def get_short_name(self):
        if self.first_name == None:
            return self.last_name
        else:
            return self.first_name 

class TutorReview(models.Model):
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rater_review', blank=True, null=True)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='tutor_review', on_delete=models.CASCADE)   
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Review for ' + str(self.tutor) + ' by ' + str(self.rater)