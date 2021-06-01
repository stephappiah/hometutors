from django.contrib.gis.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from findtutors.courses import courses_choices, programmes_choices
from findtutors.multi_choices import teach_level_choices
from django.urls import reverse

class GroupClass(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_tutor')
    title = models.CharField(max_length=50, null=True)
    programs = MultiSelectField(choices=programmes_choices, max_length=200, null=True)
    subjects = MultiSelectField(choices=courses_choices, max_length=200, null=True)
    levels = MultiSelectField(choices=teach_level_choices, max_length=200, null=True)
    course_description = models.CharField(max_length=200, null=True)
    location = models.PointField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    total_seats = models.IntegerField(null=True, blank=True)
    available_seats = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    
    

    def __str__(self):
        return str(self.tutor)

    def get_absolute_url(self):
        return reverse('groupstudy:group_class_list', kwargs={"pk": self.pk})

