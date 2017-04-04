from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import NozzleMaterial
from ..forms import NozzleMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class NozzleMaterialListView(GenericListView):
    model = NozzleMaterial
    display_data = ('chemical_formula', 'description', 'illustration')


class NozzleMaterialDetailView(DetailView):
    model = NozzleMaterial
    template_name = "catalog/chemical_detail.html"


class NozzleMaterialCreateView(GenericCreateView):
    model = NozzleMaterial
    form_class = NozzleMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("nozzle_material_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(NozzleMaterialCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("nozzle_material_detail", args=(self.object.pk,))


class NozzleMaterialUpdateView(UpdateView):
    model = NozzleMaterial
    form_class = NozzleMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(NozzleMaterialUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("nozzle_material_detail", args=(self.object.pk,))


class NozzleMaterialDeleteView(DeleteView):
    model = NozzleMaterial
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("nozzle_material_list")
