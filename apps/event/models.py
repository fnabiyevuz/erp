from django.db import models

from apps.common.models import BaseModel


class Event(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    schedule = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
