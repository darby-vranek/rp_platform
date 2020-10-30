from django.db import models
from apps.senpals.models import Model, User
from apps.verses.models import Verse


class Timeline(Model):
    user = models.ForeignKey(User, related_name='timelines', blank=True, on_delete=models.DO_NOTHING, null=True)
    verse = models.ForeignKey(Verse, related_name='timelines', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Untitled Timeline', blank=True)
    year_zero = models.OneToOneField('Event', on_delete=models.CASCADE)


class Event(Model):
    timeline = models.ForeignKey(Timeline, related_name='events')
    rank = models.SmallIntegerField()
    date = models.DateField(null=True, blank=True, default=None)
    title = models.CharField(max_length=255)