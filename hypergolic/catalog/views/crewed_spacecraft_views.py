from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import CrewedSpacecraft
from ..forms import CrewedSpacecraftForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CrewedSpacecraftListView(GenericListView):
    model = CrewedSpacecraft
    template_name = "catalog/generic_list.html"
    display_data = ('country', 'first_flight', 'fueled_weight', 'manufacturer')


class CrewedSpacecraftDetailView(DetailView):
    model = CrewedSpacecraft
    template_name = "catalog/crewed_spacecraft_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(CrewedSpacecraftDetailView, self).get_context_data(**kwargs)
        return ret


class CrewedSpacecraftCreateView(GenericCreateView):
    model = CrewedSpacecraft
    form_class = CrewedSpacecraftForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system',
    # 'battery_capacity', 'electricity_source', 'power_generation',
    # 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield',
    # 'landing_solution', 'num_flights', 'failures', 'fueled_weight',
    # 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight',
    # 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines',
    # 'tank_type', 'tank_material', 'illustration', 'crewed_spacecraft_ptr', 'crew',
    # 'life_support', 'supplies_days', 'pressurized_volume']
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("crewed_spacecraft_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CrewedSpacecraftCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_spacecraft_detail", args=(self.object.pk,))


class CrewedSpacecraftUpdateView(UpdateView):
    model = CrewedSpacecraft
    form_class = CrewedSpacecraftForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system',
    # 'battery_capacity', 'electricity_source', 'power_generation',
    # 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield',
    # 'landing_solution', 'num_flights', 'failures', 'fueled_weight',
    # 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight',
    # 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines',
    # 'tank_type', 'tank_material', 'illustration', 'crewed_spacecraft_ptr', 'crew',
    # 'life_support', 'supplies_days', 'pressurized_volume']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CrewedSpacecraftUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_spacecraft_detail", args=(self.object.pk,))


class CrewedSpacecraftDeleteView(DeleteView):
    model = CrewedSpacecraft
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("crewed_spacecraft_list")
