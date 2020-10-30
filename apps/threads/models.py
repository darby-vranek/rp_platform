from django.db import models
from django.urls import reverse
from apps.senpals.models import Model, User
from apps.verses.models import Verse
from apps.characters.models import Character
from django.forms import ModelForm
from django import forms
from django.forms.widgets import HiddenInput, Textarea


# thread models & forms
class Thread(Model):
    user = models.ForeignKey(User, related_name='starters', blank=True, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=255, default='Untitled', blank=True)
    verse = models.ForeignKey(Verse, related_name='threads', blank=True, null=True, on_delete=models.DO_NOTHING)
    caption = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.pk})

    def get_update_form(self):
        return ThreadUpdateForm(instance=self)

    def get_reply_form(self):
        return ReplyCreateForm(initial={'thread': self})

    def get_characters(self):
        characters = list()
        for reply in self.replies.all():
            if reply.character not in characters:
                characters.append(reply.character)
        characters.sort(key=lambda x: x.page_name)
        return characters

    def get_latest_reply(self):
        return self.replies.order_by('created').last()


class ThreadCreateForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    verse = forms.ModelChoiceField(queryset=Verse.objects.all(), required=False)
    caption = forms.CharField(max_length=255, required=False)
    character = forms.ModelChoiceField(queryset=Character.objects.all())
    text = forms.TextInput()


class ThreadUpdateForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'verse', 'caption']


# reply model & forms
class Reply(Model):
    character = models.ForeignKey(Character, related_name='replies', on_delete=models.DO_NOTHING, null=True)
    thread = models.ForeignKey(Thread, related_name='replies', on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ['created']

    def get_update_form(self):
        return ReplyUpdateForm(self)

    def __str__(self):
        return f"Reply by {self.character.page_name} to {self.thread.title}"


class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['thread', 'character', 'text']

        widgets = {
            'thread': HiddenInput(),
            'text': Textarea()
        }


class ReplyUpdateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['text']