from django.forms import ModelForm
from django.urls import reverse
from django import forms
from apps.senpals.models import *
from apps.characters.models import Character
from apps.verses.models import Verse


class Chat(Model):
    title = models.CharField(max_length=100, default='Untitled', blank=True)
    verse = models.ForeignKey(Verse, related_name='chats', null=True, blank=True, on_delete=models.DO_NOTHING)
    caption = models.CharField(max_length=255, default='', blank=True)
    user = models.ForeignKey(User, related_name='chats', blank=True, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character, related_name='chats')
    cover = models.URLField(blank=True, default='')
    open = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.title

    def get_line_form(self):
        return LineForm(initial={'chat': self})


class Line(Model):
    chat = models.ForeignKey(Chat, related_name='lines', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='lines', on_delete=models.CASCADE)
    icon = models.URLField(blank=True, default='')
    text = models.TextField()

    def __str__(self):
        return f"{ self.character.page_name }: {self.text}"


class ChatCreateForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    verse = forms.ModelChoiceField(queryset=Verse.objects.all(), required=False)
    cover = forms.CharField(max_length=255, required=False)
    characters = forms.ModelMultipleChoiceField(queryset=Character.objects.all())
    character = forms.ModelChoiceField(queryset=Character.objects.all(), required=True)
    icon = forms.URLField(required=False)
    text = forms.CharField(widget=forms.Textarea)


class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = ['chat', 'character', 'icon', 'text']
        widgets = {
            'chat': forms.HiddenInput()
        }

