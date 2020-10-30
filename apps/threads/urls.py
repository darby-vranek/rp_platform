from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.ThreadListView.as_view(),
         name='thread-list'),
    path('new/',
         views.ThreadCreateView.as_view(),
         name='thread-create'),
    path('<int:pk>/',
         views.ThreadDetailView.as_view(),
         name='thread-detail'),
    path('<int:pk>/edit/',
         views.ThreadUpdateView.as_view(),
         name='thread-update'),
    path('<int:pk>/delete/',
         views.ThreadDeleteView.as_view(),
         name='thread-delete'),
    path('<int:pk>/replies/new/',
         views.ReplyCreateView.as_view(),
         name='reply-create'),
    path('<int:thread_pk>/replies/<int:pk>/update/',
         views.ReplyUpdateView.as_view(),
         name='reply-update'),
    path('<int:thread_pk>/replies/<int:pk>/delete/',
         views.ReplyDeleteView.as_view(),
         name='reply-delete'),
]
