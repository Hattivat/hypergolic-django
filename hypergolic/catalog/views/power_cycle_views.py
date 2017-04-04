from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import PowerCycle
from ..forms import PowerCycleForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class PowerCycleListView(GenericListView):
    model = PowerCycle
    display_data = ('description', 'illustration')


class PowerCycleDetailView(DetailView):
    model = PowerCycle
    template_name = "catalog/generic_detail.html"


class PowerCycleCreateView(GenericCreateView):
    model = PowerCycle
    form_class = PowerCycleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("power_cycle_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(PowerCycleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("power_cycle_detail", args=(self.object.pk,))


class PowerCycleUpdateView(UpdateView):
    model = PowerCycle
    form_class = PowerCycleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(PowerCycleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("power_cycle_detail", args=(self.object.pk,))


class PowerCycleDeleteView(DeleteView):
    model = PowerCycle
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("power_cycle_list")
