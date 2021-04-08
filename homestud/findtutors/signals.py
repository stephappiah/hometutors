from django.dispatch import receiver
from django.db.models import signals
from .models import TutorProfile, TutorReview

from django_q.tasks import async_task, schedule

@receiver(signals.post_save, sender=TutorProfile)
def tutor_onboard_email(sender, instance, created, **kwargs):
    # only send on create (normal signal could fire on update, which isn't something we want)
    if created:
        # --------------------------   email variables      ----------------------------------------------
        print('email signal is fired!')
        tutor_email = instance.user.email
        first_name = instance.first_name
        tutor_slug = instance.slug
        last_name = instance.last_name
        review_url = f'https://homestud.co/tutor/{tutor_slug}/review'
        tutor_url = f'https://homestud.co/tutor/{tutor_slug}'
        admin_email = 'ad.homestud@gmail.com'

        wlc_context = {
                'first_name': first_name,
                'review_url': review_url,
            }

        adm_context = {
                'first_name': first_name,
                'tutor_url': tutor_url,
            }

        # --------------------------   end of email variables      ----------------------------------------------


        # send tutor email after profile is created
        async_task(
            'homestud.utils.notify_email',
            'findtutors/email/tutor-onboard-email.html',
            tutor_email,
            'Welcome to the Homestud community!',
            wlc_context
        )

        # email admin of new tutor profile
        async_task(
            'homestud.utils.notify_email',
            'findtutors/email/notify-admin-email.html',
            admin_email,
            f'{first_name} {last_name} signed up as a tutor!',
            adm_context
        )


    
# signal for tutor_review/recommendation model
@receiver(signals.post_save, sender=TutorReview)
def tutor_review_email(sender, instance, created, **kwargs):
    if created:
        print('new review created!')
        tutor_email = instance.tutor.email
        first_name = instance.tutor.first_name
        last_name = instance.tutor.last_name
        rater = instance.rater.get_full_name
        review = instance.comment
        
        subject = f'{rater} reviewed your tutor profile!'
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'review': review,
            'rater': rater
        }
        template = 'findtutors/email/new-tutor-review.html'
        print(f'{tutor_email}; {first_name}, {rater}, {review}')

        # send tutor an email function
        async_task(
            'homestud.utils.notify_email',
            template,
            tutor_email,
            subject,
            context
        )

    

