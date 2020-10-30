from django.forms import ModelForm
from django.urls import reverse
from apps.senpals.models import *
from apps.verses.models import Verse


class Character(Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='characters', blank=True)
    name = models.CharField(max_length=100)
    page_name = models.SlugField(max_length=25, unique=True)
    tagline = models.CharField(max_length=25, default='', blank=True)
    description = models.TextField(blank=True)
    icon = models.URLField(default='', blank=True)
    header_image = models.URLField(default='', blank=True)

    def __str__(self):
        return self.page_name

    class Meta:
        ordering = ['page_name']

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'page_name': self.page_name})

    def get_threads(self):
        threads = list()
        for reply in self.replies.all():
            if reply.thread not in threads:
                threads.append(reply.thread)
        return threads


class CharacterCreateForm(ModelForm):
    class Meta:
        model = Character
        fields = ['page_name', 'name', 'tagline', 'description', 'icon', 'header_image']
