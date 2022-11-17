import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Transaction(models.Model):
    class Types(models.TextChoices):
        EXPENSE = ('E', 'Expense')
        INCOME = ('I', 'Income')

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=Types.choices)

    def __str__(self):
        return str(self.amount)


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name
