from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_musician = models.BooleanField(
        verbose_name = "Is Musician",
        null = True,
    )