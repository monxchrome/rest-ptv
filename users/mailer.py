from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER


def notify_admin_new_user(email):
    date = str(timezone.now())
    admin_email = EMAIL_HOST_USER
    users = ['1@mail.com', '2@mail.com', '3@mail.com']
    for user in users:
        send_mail(
            'Новий користувач був створений',
            f'Користувач з поштою {email} був створений {date}',
            'admin@example.com',
            [user],
            fail_silently=False,
        )
