import datetime

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Sum
from django.conf import settings

from celery import shared_task

from expense_tracker.core.models import Transaction


@shared_task
def send_statistics():
    for user in get_user_model().objects.all():
        subject = 'EXPENSE ACCOUNTING MANAGER'
        sum_of_transactions = Transaction.objects.filter(
            user=user,
            date__range=[
                datetime.date.today(),
                datetime.date.today() - datetime.timedelta(days=1)]
        ).aggregate(Sum('amount'))
        message = f'Сумма транзакций за последние 24 часа: {sum_of_transactions.get("ammount__sum", 0)}'
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email],
                  fail_silently=False)
