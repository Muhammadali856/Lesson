from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


def send_email_confirmation(request, user):
    token = default_token_generator.make_token(user)
    vid = user.pk

    confirmation_link = request.build_absolute_url(
        reverse(viewname='users:confirm_email', kwargs={'vid': vid, 'token': token})
    )

    subject = 'Email Confirmation'  
    html_message = render_to_string('users/email_confirmation.html',{
        'user': user,
        'confirmation_link': confirmation_link
    })


    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email.content_subtype = 'html'
    email.send()