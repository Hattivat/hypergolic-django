from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import HeatshieldMaterial
from ..forms import HeatshieldMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class HeatshieldMaterialListView(GenericListView):
    model = HeatshieldMaterial
    display_data = ('chemical_formula', 'description', 'illustration')


class HeatshieldMaterialDetailView(DetailView):
    model = HeatshieldMaterial
    template_name = "catalog/chemical_detail.html"


class HeatshieldMaterialCreateView(GenericCreateView):
    model = HeatshieldMaterial
    form_class = HeatshieldMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("heatshield_material_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(HeatshieldMaterialCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("heatshield_material_detail", args=(self.object.pk,))


class HeatshieldMaterialUpdateView(UpdateView):
    model = HeatshieldMaterial
    form_class = HeatshieldMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(HeatshieldMaterialUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("heatshield_material_detail", args=(self.object.pk,))


class HeatshieldMaterialDeleteView(DeleteView):
    model = HeatshieldMaterial
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("heatshield_material_list")
