from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_confirm_email(email, token):
    confirm_url = f"{settings.BASE_URL}api/v1/register/confirm/{token}"
    subject = "Confirm your Email"
    message = f"Click on this link to confirm your email: {confirm_url}"
    send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
