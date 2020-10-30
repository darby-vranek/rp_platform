"""project_senpals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.senpals.urls')),
    path('characters/', include('apps.characters.urls')),
    path('chats/', include('apps.chats.urls')),
    path('verses/', include('apps.verses.urls')),
    path('threads/', include('apps.threads.urls')),
    path('posts/', include('apps.posts.urls')),
    path('icons/', include('apps.icons.urls')),
    # path('wireframe/', include('apps.wireframe.urls')), # for testing new layouts/etc, not in use
]