from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Spacecraft
from ..forms import SpacecraftForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SpacecraftListView(GenericListView):
    model = Spacecraft
    template_name = "catalog/generic_list.html"
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
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system',
    # 'battery_capacity', 'electricity_source', 'power_generation',
    # 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield',
    # 'landing_solution', 'num_flights', 'failures', 'fueled_weight',
    # 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight',
    # 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines',
    # 'tank_type', 'tank_material', 'illustration']
    template_name = "catalog/generic_create.html"
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
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system',
    # 'battery_capacity', 'electricity_source', 'power_generation',
    # 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield',
    # 'landing_solution', 'num_flights', 'failures', 'fueled_weight',
    # 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight',
    # 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines',
    # 'tank_type', 'tank_material', 'illustration']
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
