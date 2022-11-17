from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from expense_tracker.authentication.models import Profile
from expense_tracker.core.models import Category, Transaction
from expense_tracker.core.constants import DEFAULT_CATEGORIES


@receiver(post_save, sender=get_user_model())
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        default_categories = [Category(user=instance, name=cat) for cat in DEFAULT_CATEGORIES]
        Category.objects.bulk_create(default_categories)


@receiver(post_save, sender=Transaction)
def change_balance(sender, instance, created, **kwargs):
    profile = Profile.objects.get(user=instance.user)
    transactions = Transaction.objects.filter(user=instance.user)
    e_transactions = sum(transactions.filter(type='E').values_list('amount', flat=True))
    i_transactions = sum(transactions.filter(type='I').values_list('amount', flat=True))
    profile.balance = i_transactions - e_transactions
    profile.save()
