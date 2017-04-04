from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import TankConstruction
from ..forms import TankConstructionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class TankConstructionListView(GenericListView):
    model = TankConstruction
    display_data = ('description', 'illustration')


class TankConstructionDetailView(DetailView):
    model = TankConstruction
    template_name = "catalog/generic_detail.html"


class TankConstructionCreateView(GenericCreateView):
    model = TankConstruction
    form_class = TankConstructionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("tank_construction_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(TankConstructionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("tank_construction_detail", args=(self.object.pk,))


class TankConstructionUpdateView(UpdateView):
    model = TankConstruction
    form_class = TankConstructionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(TankConstructionUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("tank_construction_detail", args=(self.object.pk,))


class TankConstructionDeleteView(DeleteView):
    model = TankConstruction
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("tank_construction_list")
