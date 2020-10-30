from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.ChatListView.as_view(),
         name='chat-list'),
    path('new/',
         views.ChatCreateView.as_view(),
         name='chat-create'),
    path('<int:pk>/',
         views.ChatDetailView.as_view(),
         name='chat-detail'),
    path('<int:pk>/edit/',
         views.ChatUpdateView.as_view(),
         name='chat-update'),
    path('<int:pk>/delete/',
         views.ChatDetailView.as_view(),
         name='chat-delete'),
    path('lines/new/',
         views.LineCreateView.as_view(),
         name='line-create'),
    path('lines/<int:pk>/edit/',
         views.LineUpdateView.as_view(),
         name='line-update'),
    path('lines/<int:pk>/delete/',
         views.LineDeleteView.as_view(),
         name='line-delete')
]