from django.db import models
from django_extensions.db.models import TimeStampedModel
import uuid


class Study(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.TextField(default='my study', max_length=100)
    description = models.TextField(default='my description', max_length=1024)
    researchers = models.ManyToManyField('user.User')

    class Software(models.TextChoices):
        JSPSYCH = "JP", "jsPsych"  # https://www.jspsych.org/7.3/
        PSYCHOPY = "PS", "psychoJS"
        SURVEYJS = "SJ", "surveyJS"

    class Status(models.TextChoices):
        RUN = "RU", "Running"
        STOP = 'SJ', "Stopped"

    software = models.CharField(max_length=2, choices=Software.choices)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.STOP)
