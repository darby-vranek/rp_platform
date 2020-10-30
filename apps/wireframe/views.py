from apps.characters.models import Character
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
