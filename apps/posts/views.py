from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from apps.verses.models import Verse
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'wireframe/posts/post_list_page.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'wireframe/posts/post_form_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verses'] = Verse.objects.all()
        context['characters'] = Character.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'wireframe/posts/post_detail_page.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'wireframe/posts/post_form_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verses'] = Verse.objects.all()
        context['characters'] = Character.objects.all()
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
