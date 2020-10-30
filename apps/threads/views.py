from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import *
from django.urls import reverse_lazy


class ThreadCreateView(FormView):
    template_name = 'threads/thread_create_page.html'
    form_class = ThreadCreateForm

    def form_valid(self, form):
        thread = self.create_thread(form, self.request.user)
        self.create_reply(form, thread)
        self.success_url = reverse_lazy('thread-detail', kwargs={'pk': thread.pk})
        return super().form_valid(form)

    def create_thread(self, form, user):
        if form.fields['verse']:
            verse = form.cleaned_data['verse']
        else:
            verse = None
        thread = Thread.objects.create(
            user=user,
            title=form.cleaned_data['title'],
            verse=verse,
            caption=form.cleaned_data['caption']
        )
        thread.save()
        return thread

    def create_reply(self, form, thread):
        reply = Reply.objects.create(
            character=form.cleaned_data['character'],
            thread=thread,
            text=form.cleaned_data['text']
        )
        reply.save()


class ThreadListView(ListView):
    model = Thread
    template_name = 'threads/thread_list_page.html'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'wireframe/threads/thread_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_form'] = self.object.get_reply_form()
        return context


class ThreadUpdateView(UpdateView):
    model = Thread
    form_class = ThreadUpdateForm

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = reverse('thread-detail', kwargs={'pk': pk})
        return super().post(self)


class ThreadDeleteView(DeleteView):
    model = Thread
    success_url = reverse_lazy('thread-list')


class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyCreateForm
    thread = None

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = reverse_lazy('thread-detail', kwargs={'pk': pk})
        return super().post(self)

    def form_valid(self, form):
        return super().form_valid(form)


class ReplyUpdateView(UpdateView):
    model = Reply
    form_class = ReplyUpdateForm
    template_name = "senpals/form.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('thread-detail', kwargs={'pk': kwargs['thread_pk']})
        return super().post(self)


class ReplyDeleteView(DeleteView):
    model = Reply

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('thread-detail', kwargs={'pk': kwargs['thread_pk']})
        return super().post(self)
