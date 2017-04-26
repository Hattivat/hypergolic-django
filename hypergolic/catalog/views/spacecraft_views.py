from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Spacecraft
from catalog.forms import SpacecraftForm
from catalog.filters import SpacecraftFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SpacecraftListView(GenericListView):
    model = Spacecraft
    f = SpacecraftFilter
    display_data = ('country', 'first_flight', 'fueled_weight', 'manufacturer')


class SpacecraftDetailView(DetailView):
    model = Spacecraft
    template_name = "catalog/spacecraft_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(SpacecraftDetailView, self).get_context_data(**kwargs)
        return ret


class SpacecraftCreateView(GenericCreateView):
    model = Spacecraft
    form_class = SpacecraftForm
    success_url = reverse_lazy("spacecraft_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(SpacecraftCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("spacecraft_detail", args=(self.object.pk,))


class SpacecraftUpdateView(UpdateView):
    model = Spacecraft
    form_class = SpacecraftForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(SpacecraftUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("spacecraft_detail", args=(self.object.pk,))


class SpacecraftDeleteView(DeleteView):
    model = Spacecraft
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("spacecraft_list")
