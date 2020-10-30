from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from apps.characters.models import Character
from apps.chats.models import Chat, Line
from apps.posts.models import Post
from apps.threads.models import Thread, Reply


def home(request):
    return render(request, 'senpals/home_page.html', context={'characters': Character.objects.count(),
                                                              'chats': Chat.objects.count(),
                                                              'lines': Line.objects.count(),
                                                              'posts': Post.objects.count(),
                                                              'threads': Thread.objects.count(),
                                                              'replies': Reply.objects.count()
                                                              })


def users(request):
    return render(request, 'senpals/user_list_page.html', context={'users': User.objects.all()})


def user(request, username):
    return render(request, 'senpals/user_profile_page.html', context={'profile': get_object_or_404(User, username=username)})
