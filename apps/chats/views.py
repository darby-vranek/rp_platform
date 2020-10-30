from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import *
from django.urls import reverse_lazy


class ChatListView(ListView):
    model = Chat
    template_name = 'wireframe/chats/chat_list_page.html'


class ChatCreateView(FormView):
    template_name = 'wireframe/chats/chat_create_page.html'
    form_class = ChatCreateForm

    def form_valid(self, form):
        chat = self.create_chat(form, self.request.user)
        self.create_line(form, chat)
        self.success_url = reverse_lazy('chat-detail', kwargs={'pk': chat.pk})
        return super().form_valid(form)

    def create_chat(self, form, user):
        if form.fields['verse']:
            verse = form.cleaned_data['verse']
        else:
            verse = None
        chat = Chat.objects.create(
            user=user,
            title=form.cleaned_data['title'],
            verse=verse,
            caption=form.cleaned_data['caption']
        )
        chat.characters.set(form.cleaned_data['characters'])
        chat.save()
        return chat

    def create_line(self, form, chat):
        line = Line.objects.create(
            character=form.cleaned_data['character'],
            chat=chat,
            icon=form.cleaned_data['icon'],
            text=form.cleaned_data['text']
        )
        line.save()


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'wireframe/chats/chat_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['line_form'] = self.object.get_line_form()
        return context


class ChatUpdateView(UpdateView):
    pass


class ChatDeleteView(DeleteView):
    model = Chat
    success_url = reverse_lazy('chat-list')


class LineCreateView(CreateView):
    form_class = LineForm
    template_name = 'wireframe/chats/chat_detail_page.html'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('chat-detail', kwargs={'pk': request.POST['chat']})
        return super().post(self)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class LineUpdateView(UpdateView):
    model = Line
    form_class = LineForm

    def post(self, request, *args, **kwargs):
        line = Line.objects.get(pk=kwargs['pk'])
        self.success_url = reverse_lazy('chat-detail', kwargs={'pk': line.chat.pk})
        return super().post(self)


class LineDeleteView(DeleteView):
    pass
