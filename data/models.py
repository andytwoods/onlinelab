from django.db import models
from django_extensions.db.models import TimeStampedModel


class Result(TimeStampedModel):
    study = models.ForeignKey('study.Study', null=True, on_delete=models.SET_NULL)
    participant = models.ForeignKey('user.User', default=None, null=True, on_delete=models.SET_NULL)
    data = models.JSONField()
