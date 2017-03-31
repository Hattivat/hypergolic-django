from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Engine
from ..forms import EngineForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class EngineListView(GenericListView):
    model = Engine
    display_data = ('country', 'developed', 'application',
                    'propellants', 'cycle', 'specific_impulse_vac',
                    'thrust_vac', 'twr')


class EngineDetailView(DetailView):
    model = Engine
    template_name = "catalog/engine_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(EngineDetailView, self).get_context_data(**kwargs)
        return ret


class EngineCreateView(GenericCreateView):
    model = Engine
    form_class = EngineForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'application', 'propellants', 'mixture_ratio',
    # 'cycle', 'specific_impulse_vac', 'specific_impulse_sl', 'thrust_sl',
    # 'thrust_vac', 'twr', 'chamber_pressure', 'combustion_chambers',
    # 'rated_burn_time', 'nozzle_ratio', 'nozzle_shape', 'nozzle_material',
    # 'cooling_method', 'injector_type', 'coefficient_of_thrust_vac',
    # 'coefficient_of_thrust_sl', 'ignition_method', 'restart_capability',
    # 'num_restarts', 'throttle_range_min', 'throttle_range_max',
    # 'illustration']
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("engine_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EngineCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineUpdateView(UpdateView):
    model = Engine
    form_class = EngineForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'dry_weight', 'application', 'propellants', 'mixture_ratio',
    # 'cycle', 'specific_impulse_vac', 'specific_impulse_sl', 'thrust_sl',
    # 'thrust_vac', 'twr', 'chamber_pressure', 'combustion_chambers',
    # 'rated_burn_time', 'nozzle_ratio', 'nozzle_shape', 'nozzle_material',
    # 'cooling_method', 'injector_type', 'coefficient_of_thrust_vac',
    # 'coefficient_of_thrust_sl', 'ignition_method', 'restart_capability',
    # 'num_restarts', 'throttle_range_min', 'throttle_range_max',
    # 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EngineUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineDeleteView(DeleteView):
    model = Engine
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("engine_list")
