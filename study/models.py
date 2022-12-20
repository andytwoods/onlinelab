from django.db import models
from django_extensions.db.models import TimeStampedModel
import uuid


class Study(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.TextField(default='my study')
    description = models.TextField(default='my description')

    class Software(models.TextChoices):
        JSPSYCH = "JP", "JS psych"  # https://www.jspsych.org/7.3/
        PSYCHOPY = "PS", "Psycho JS"
        SURVEYJS = 'SJ', "Survey JS"

    class Status(models.TextChoices):
        RUN = "RU", "Running"
        STOP = 'SJ', "Stopped"

    software = models.CharField(
        max_length=2, choices=Software.choices
    )

    status = models.CharField(max_length=2, choices=Status.choices, description=Status.STOP)
