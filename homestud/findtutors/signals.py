from django.dispatch import receiver
from django.db.models import signals
from .models import TutorProfile
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

@receiver(signals.post_save, sender=TutorProfile)
def tutor_onboard_email(sender, instance, created, **kwargs):
    # only send on create (normal signal could fire on update, which isn't something we want)
    if created:
        print('email signal is fired!')
        tutor_email = instance.user.email
        first_name = instance.first_name
        tutor_slug = instance.slug
        last_name = instance.last_name
        # send tutor an email function
        def email_tutor():   
            review_url = f'https://homestud.co/tutor/{tutor_slug}/review'
            subject = 'Welcome to the Homestud community!'
            context = {
                'first_name': first_name,
                'review_url': review_url,
            }
            template = get_template('findtutors/email/tutor-onboard-email.html')
            html_message = template.render(context)
            text_message = strip_tags(html_message)

            send_mail(
                        subject,
                        text_message,
                        'Homestud <hello@homestud.co>',
                        [f'{tutor_email}'],
                        html_message=html_message
                )
        
        email_tutor()

        def email_admin():
            admin_email = 'ad.homestud@gmail.com'
            tutor_url = f'https://homestud.co/tutor/{tutor_slug}'

            print('fname:', first_name)
            print('email:', admin_email)
            print('review_url:', tutor_url)

            subject = f'{first_name} {last_name} signed up as a tutor!'
            context = {
                'first_name': first_name,
                'tutor_url': tutor_url,
            }
            template = get_template('findtutors/email/notify-admin-email.html')
            html_message = template.render(context)
            text_message = strip_tags(html_message)

            send_mail(
                        subject,
                        text_message,
                        'Homestud <hello@homestud.co>',
                        [admin_email],
                        html_message=html_message
                )
        
        email_admin()

    
            

