from django.db.models import Sum, Q
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from expense_tracker.core.models import Category, Transaction
from expense_tracker.core.constants import DEFAULT_CATEGORIES


@receiver(post_save, sender=get_user_model())
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        default_categories = [Category(user=instance, name=cat) for cat in DEFAULT_CATEGORIES]
        Category.objects.bulk_create(default_categories)


@receiver(post_save, sender=Transaction)
def change_balance(sender, instance, created, **kwargs):
    transaction_amount = Transaction.objects.filter(user=instance.user).aggregate(
        i_transaction_sum=Sum('amount', filter=Q(type='I')), e_transaction_sum=Sum('amount', filter=Q(type='E')))
    instance.user.profile.balance = transaction_amount['i_transaction_sum'] - transaction_amount['e_transaction_sum']
    instance.user.profile.save()
