from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.CharacterListView.as_view(),
         name='character-list'),
    path('new/',
         views.CharacterCreateView.as_view(),
         name='character-create'),
    path('<slug:page_name>/',
         views.CharacterDetailView.as_view(),
         name='character-detail'),
]
