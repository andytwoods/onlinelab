from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_experimenter = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=False)