# from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django_q.tasks import async_task, schedule
from multiselectfield import MultiSelectField

from .courses import courses_choices, programmes_choices
from .multi_choices import (class_type_choices, free_lesson_choices,
                            highest_education_choices, teach_level_choices,
                            user_type_choices)


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

    # admin role edit for reviewing tutor substandard profile
    admin_show = models.BooleanField(default=False, blank=True)
    admin_comment = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # below attribute helps track change in admin_profile_status and admin comment
    # this is cached and compared with the actual attribute to spot any changes
    # it is then used to decide whether to notify users or admin of change
    __original_admin_show = None
    __original_admin_comment = None

    # __original_admin_profile_status to be compared with admin_profile_status in signal
    # this helps send an email on change
    def __init__(self, *args, **kwargs):
        super(TutorProfile, self).__init__(*args, **kwargs)
        self.__original_admin_show = self.admin_show
        self.__original_admin_comment = self.admin_comment

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

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # save __original_admin_show to avoid error

        # below triggers if admin_show or admin comment changes
        # it is being compared to __original_admin_show which
        # is cached
        # the code actually means, send email if admin_show or admin_comment changes
        if self.admin_show != self.__original_admin_show or self.admin_comment != self.__original_admin_comment:
            print('admin changed tutor status!')
            tutor_email = self.user.email
            tutor_slug = self.slug
            first_name = self.first_name
            tutor_url = f'https://homestud.co/tutor/{tutor_slug}'
            tutor_review_url = f'https://homestud.co/tutor/{tutor_slug}/review'
            review_comment = self.admin_comment
            
            print(tutor_email)
            # admin_show is true 
            # email is sent to user if admin sets self.admin_show to true
            if self.admin_show is True:
                print('tutor is live')
                subject = 'Hurray! Your tutor profile is live on Homestud'
                context = {
                    'tutor_url': tutor_url,
                    'first_name': first_name,
                    'tutor_review_url': tutor_review_url
                }
                template = 'findtutors/email/tutor-live-email.html'
                
                # notify tutor
                async_task(
                    'homestud.utils.notify_email',
                    template,
                    tutor_email,
                    subject,
                    context
                )

            elif self.admin_show is False or self.admin_comment != self.__original_admin_comment:  # self.admin_show is False or self.admin_comment changes
                print('tutor is offline')
                subject = 'Make changes to your tutor profile'
                template = 'findtutors/email/tutor-off-email.html'
                context = {
                    'tutor_url': tutor_url,
                    'first_name': first_name,
                    'review_comment': review_comment
                }
                # send tutor email so they make changes to their profile
                async_task(
                    'homestud.utils.notify_email',
                    template,
                    tutor_email,
                    subject,
                    context
                )
        else:
            pass
            #  self.admin_show didn't change

        # if save method is updating, self.pk doesn't return None
        # then check if self.__original_admin_show == False 
        # __original_admin_show returns false when tutor is previously disabled and asked to make changes to their profile
        # send email notification to admin for review
        if self.pk is not None:
            print('tutor profile updated!')
            # tutor isn't live and is updating
            # send admin notification for profile review
            # issue!! --fix: notification email is also sent on tutor onboarding as...
            # it saves the model on different page loads
            if self.__original_admin_show is False and self.admin_show is False:
                # variables
                tutor_slug = self.slug
                first_name = self.first_name
                last_name = self.last_name
                admin_email = 'ad.homestud@gmail.com'
                tutor_url = f'https://homestud.co/tutor/{tutor_slug}'
                subject = f'Review changes for {first_name} {last_name}!'
                template = 'findtutors/email/notify-admin-tutor-review.html'
                context = {
                    'first_name': first_name,
                    'tutor_url': tutor_url,
                    'last_name': last_name,
                }
                # tutor isn't live and is updating
                # send email to admin to review changes made by tutor
                
                async_task(
                    'homestud.utils.notify_email',
                    template,
                    admin_email,
                    subject,
                    context
                )
            
            else:
                pass
        
        super(TutorProfile, self).save(force_insert, force_update, *args, **kwargs)
        # update __oringinal to related attribute when saving
        self.__original_admin_show = self.admin_show
        self.__original_admin_comment = self.admin_comment

class TutorReview(models.Model):
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rater_review', blank=True, null=True)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='tutor_review', on_delete=models.CASCADE)   
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Review for ' + str(self.tutor) + ' by ' + str(self.rater)
