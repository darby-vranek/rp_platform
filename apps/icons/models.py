from django.urls import reverse
from django import forms
from django.forms import ModelForm
from apps.senpals.models import *


class FaceClaim(Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('faceclaim-detail', kwargs={'slug': self.slug})


class Icon(Model):
    faceclaim = models.ForeignKey(FaceClaim, related_name='icons', on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField(default='https://hsto.org/getpro/habr/post_images/6ed/d94/57e/6edd9457ec4ef14fd413377a3cfb0fb4.png')
    user = models.ForeignKey(User, related_name='icons', on_delete=models.DO_NOTHING, null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('faceclaim-detail', kwargs={'slug': self.faceclaim.slug})


class IconCreateForm(ModelForm):
    class Meta:
        model = Icon
        fields = ['faceclaim', 'image', 'tags']
        widgets = {
            'tags': forms.TextInput(attrs={
                'class': 'tagsinput form-control',
                'data-role': 'tagsinput',
                'data-color': 'primary',
                'placeholder': 'add tag'
            }),
            'image': forms.ClearableFileInput(attrs={
                'multiple': True
            }),
            'faceclaim': forms.HiddenInput()

        }


class Collection(Model):
    faceclaim = models.ForeignKey(FaceClaim, related_name='collections', on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=50, blank=True)
    source = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='collections', on_delete=models.DO_NOTHING, null=True, blank=True)
    icons = models.ManyToManyField(Icon, related_name='collections')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'slug': self.faceclaim.slug, 'pk': self.pk})


class CollectionCreateForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['title', 'source', 'icons']