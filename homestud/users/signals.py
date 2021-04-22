from django.dispatch import receiver
from django.db.models import signals
from .models import User
from findtutors.models import UserProfile


# this signal saves new user's first and last names to 
# the UserProfile model so it can be updated later.
# not doing this makes it hard to create two views 
# one for update tutorprofile and another for create 

@receiver(signals.post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    
    if created:
        # create user profile for new user
        UserProfile.objects.create(
            user=instance, 
            first_name=instance.first_name,
            last_name=instance.last_name
            )

        instance.user_profile.save()
        
        print('user profile created!')

