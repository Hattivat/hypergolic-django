from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import TankMaterial
from ..forms import TankMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class TankMaterialListView(GenericListView):
    model = TankMaterial
    display_data = ('description', 'illustration')


class TankMaterialDetailView(DetailView):
    model = TankMaterial
    template_name = "catalog/generic_detail.html"


class TankMaterialCreateView(GenericCreateView):
    model = TankMaterial
    form_class = TankMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("tank_material_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankMaterialCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("tank_material_detail", args=(self.object.pk,))


class TankMaterialUpdateView(UpdateView):
    model = TankMaterial
    form_class = TankMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankMaterialUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("tank_material_detail", args=(self.object.pk,))


class TankMaterialDeleteView(DeleteView):
    model = TankMaterial
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("tank_material_list")
