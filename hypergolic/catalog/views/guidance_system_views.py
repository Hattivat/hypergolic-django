from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import GuidanceSystem
from ..forms import GuidanceSystemForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class GuidanceSystemListView(GenericListView):
    model = GuidanceSystem
    display_data = ('energy_consumption', 'description', 'illustration')


class GuidanceSystemDetailView(DetailView):
    model = GuidanceSystem
    template_name = "catalog/electric_detail.html"


class GuidanceSystemCreateView(GenericCreateView):
    model = GuidanceSystem
    form_class = GuidanceSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("guidance_system_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GuidanceSystemCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("guidance_system_detail", args=(self.object.pk,))


class GuidanceSystemUpdateView(UpdateView):
    model = GuidanceSystem
    form_class = GuidanceSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GuidanceSystemUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("guidance_system_detail", args=(self.object.pk,))


class GuidanceSystemDeleteView(DeleteView):
    model = GuidanceSystem
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("guidance_system_list")
