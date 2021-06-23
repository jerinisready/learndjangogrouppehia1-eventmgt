from django.db import models

# Create your models here.
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    event_datetime = models.DateTimeField()
    is_registration_closed = models.BooleanField(default=False)
    max_no_participants = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    position = models.CharField(default="Participant", max_length=12, choices=[
         ("Participant", "Participant"),
         ("First", "First"),
         ("Second", "Second"),
         ("Third", "Third"),
    ])

    def __str__(self):
        return f"{self.event} - {self.user}"
