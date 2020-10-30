from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # user auth stuff
    path('login/', auth_views.LoginView.as_view(
        template_name='senpals/landing_page.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # user profile stuff
    path('users/', views.users, name='user-list'),
    path('users/<slug:username>/', views.user, name='user-profile')
]