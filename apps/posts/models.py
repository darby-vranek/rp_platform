from django.db import models
from django.urls import reverse
from apps.senpals.models import Model, User
from apps.characters.models import Character
from apps.verses.models import Verse
from django.forms import ModelForm
from react.render import render_component
from django.forms.widgets import HiddenInput


class Post(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', blank=True)
    title = models.CharField(max_length=100, default='Untitled', blank=True)
    text = models.TextField(blank=True)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='posts')
    verse = models.ForeignKey(Verse, on_delete=models.DO_NOTHING, related_name='posts', blank=True, null=True)
    cover = models.URLField(blank=True, default='')

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def posted_by(self):
        return f"written by {self.user.username}"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'character', 'verse', 'text', 'cover']
