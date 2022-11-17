from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Sum

from config.celery import app
from expense_tracker.core.models import Transaction


@app.task
def send_beat_statistics() -> None:
    for user in get_user_model().objects.all():
        subject = 'EXPENSE ACCOUNTING MANAGER'
        sum_of_transactions = Transaction.objects.filter(user=user).aggregate(Sum('amount'))
        message = f'Сумма транзакций за последние 24 часа: {sum_of_transactions.get("ammount__sum", 0)}'
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email],
                  fail_silently=False)
