from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.FaceClaimListView.as_view(),
         name='faceclaim-list'),
    path('new/',
         views.FaceClaimCreateView.as_view(),
         name='faceclaim-create'),
    path('<slug:slug>/',
         views.FaceClaimDetailView.as_view(),
         name='faceclaim-detail'),
    path('<slug:slug>/edit/',
         views.FaceClaimUpdateView.as_view(),
         name='faceclaim-update'),
    path('<slug:slug>/new/',
         views.IconCreateView.as_view(),
         name='icon-create'),
    path('<slug:slug>/collections/new/',
         views.CollectionCreateView.as_view(),
         name='collection-create'),
    path('<slug:slug>/collections/<int:pk>/',
         views.CollectionDetailView.as_view(),
         name='collection-detail'),
    path('<slug>/collections/<int:pk>/edit/',
         views.CollectionUpdateView.as_view(),
         name='collection-update'),
    path('<slug>/collections/<int:pk>/delete/',
         views.CollectionDeleteView.as_view(),
         name='collection-delete')
]