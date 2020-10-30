from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse


class VerseListView(ListView):
    model = Verse
    template_name = 'verses/verse_list_page.html'


class VerseCreateView(CreateView):
    model = Verse
    form_class = VerseCreateForm
    template_name = 'verses/verse_create_page.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class VerseDetailView(DetailView):
    model = Verse
    template_name = 'verses/verse_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verse_form'] = self.object.get_form()
        return context


class VerseUpdateView(UpdateView):
    model = Verse
    form_class = VerseCreateForm

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = reverse('verse-detail', kwargs={'pk': pk})
        return super().post(self)
