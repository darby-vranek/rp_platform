from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.CharacterListView.as_view()),
    path('characters/<slug:page_name>/', views.CharacterDetailView.as_view(), name='character-wire'),
]
