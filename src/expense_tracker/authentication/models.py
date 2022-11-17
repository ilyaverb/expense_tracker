import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    email = models.EmailField()

    def __str__(self):
        return str(self.uid)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)

    def __str__(self):
        return f"PROFILE: {self.user.username}"
