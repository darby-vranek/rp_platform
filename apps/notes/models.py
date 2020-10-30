from django.db import models
from apps.senpals.models import *
from apps.characters.models import Character
from apps.verses.models import Verse


class Note(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="", blank=True)
    characters = models.ManyToManyField(Character, blank=True)
    verses = models.ManyToManyField(Verse, blank=True)
    text = models.TextField(blank=True)
    tags = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text if not self.title else f'{self.title}: {self.text}'


