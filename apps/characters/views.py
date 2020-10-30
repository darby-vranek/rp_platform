from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *


class CharacterListView(ListView):
    model = Character
    template_name = 'wireframe/characters/character_list_page.html'

    def get_queryset(self):
        return Character.objects.order_by('page_name')


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'wireframe/characters/character_detail_page.html'
    slug_field = 'page_name'
    slug_url_kwarg = 'page_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterCreateForm
    template_name = 'characters/character_create_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
