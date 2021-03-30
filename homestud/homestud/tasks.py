from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

from celery import shared_task

@shared_task
def notify_email(template, recipient, subject, context, sender='Homestud <hello@homestud.co>'):
    """
    sends an email to user when an action happens

    :param str template: path to template ex: 'findtutors/email/notify-admin-tutor-review.html'
    :param str recipient: The recipient of the message
    :param str subject: subject of the message
    :param str sender: The sender of the message. Defaults to hello@homestud.co
    :param dict context: context to be used in template. ex: {'name': name}

    """

    sub = subject
    contxt = context

    temp = get_template(template)
    html_message = temp.render(context)
    text_message = strip_tags(html_message)

    return send_mail(sub, text_message, sender, [recipient],html_message=html_message)