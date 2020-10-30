from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.utils.text import slugify
from django.urls import reverse_lazy


class FaceClaimListView(ListView):
    model = FaceClaim
    template_name = 'icons/face_claim_list_page.html'


class FaceClaimCreateView(CreateView):
    model = FaceClaim
    # form_class = FaceClaimForm

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


class FaceClaimDetailView(DetailView):
    model = FaceClaim
    template_name = 'icons/face_claim_detail_page.html'


class FaceClaimUpdateView(UpdateView):
    pass


class IconCreateView(CreateView):
    model = Icon
    form_class = IconCreateForm
    template_name = 'icons/icon_create_page.html'

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('image')
        for f in files:
            Icon.objects.create(
                faceclaim=FaceClaim.objects.get(slug=kwargs['slug']),
                image=f
            )
        return redirect(reverse('faceclaim-detail', kwargs={'slug': kwargs['slug']}))


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionCreateForm
    template_name = 'icons/collection_create_page.html'
    fc = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CollectionCreateForm(initial={'faceclaim': kwargs['slug']})
        return context

    def post(self, request, *args, **kwargs):
        self.fc = FaceClaim.objects.get(slug=kwargs['slug'])
        return super().post(self)

    def form_valid(self, form):
        form.instance.faceclaim = self.fc
        form.instance.user = self.request.user
        return super().form_valid(form)


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'icons/collection_detail_page.html'


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionCreateForm
    template_name = 'icons/collection_create_page.html'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('collection-detail', kwargs={'slug': kwargs['slug'], 'pk': kwargs['pk']})
        return super().post(self)


class CollectionDeleteView(DeleteView):
    pass
