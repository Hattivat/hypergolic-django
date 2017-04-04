from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Manufacturer
from ..forms import ManufacturerForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class ManufacturerListView(GenericListView):
    model = Manufacturer
    display_data = ('country', 'established', 'active', 'defunct')


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "catalog/manufacturer_detail.html"


class ManufacturerCreateView(GenericCreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("manufacturer_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(ManufacturerCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("manufacturer_detail", args=(self.object.pk,))


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(ManufacturerUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("manufacturer_detail", args=(self.object.pk,))


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("manufacturer_list")
