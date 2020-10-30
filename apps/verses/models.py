from django.db import models
from django.forms import ModelForm
from apps.senpals.models import Model, User


class Verse(Model):
    admin = models.ForeignKey(User, related_name='admin_verses', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_form(self):
        return VerseCreateForm(instance=self)


class VerseCreateForm(ModelForm):
    class Meta:
        model = Verse
        fields = ['name', 'franchise', 'description']
