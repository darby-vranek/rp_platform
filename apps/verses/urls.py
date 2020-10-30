from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.VerseListView.as_view(),
         name='verse-list'),
    path('new/',
         views.VerseCreateView.as_view(),
         name='verse-create'),
    path('<int:pk>/',
         views.VerseDetailView.as_view(),
         name='verse-detail'),
    path('<int:pk>/edit/',
         views.VerseUpdateView.as_view(),
         name='verse-update'),
]
