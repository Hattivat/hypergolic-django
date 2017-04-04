from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Stage
from ..forms import StageForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StageListView(GenericListView):
    model = Stage
    template_name = "catalog/generic_list.html"
    display_data = ('country', 'developed', 'fueled_weight', 'stage_role',
                    'main_engine', 'aux_engine', 'country', 'manufacturer',
                    'tank_type')


class StageDetailView(DetailView):
    model = Stage
    template_name = "catalog/stage_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(StageDetailView, self).get_context_data(**kwargs)
        return ret


class StageCreateView(GenericCreateView):
    model = Stage
    form_class = StageForm
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
    success_url = reverse_lazy("stage_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(StageCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageUpdateView(UpdateView):
    model = Stage
    form_class = StageForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of',
    # 'native_name', 'manufacturer', 'developed', 'first_flight', 'height',
    # 'diameter', 'stage_role', 'dry_weight', 'fueled_weight',
    # 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight',
    # 'main_engine', 'num_main_engines', 'main_gimbal_yaw_min',
    # 'main_gimbal_yaw_max', 'main_gimbal_pitch_min', 'main_gimbal_pitch_max',
    # 'aux_engine', 'num_aux_engines', 'aux_gimbal_yaw_min',
    # 'aux_gimbal_yaw_max', 'aux_gimbal_pitch_min', 'aux_gimbal_pitch_max',
    # 'tank_type', 'tank_material', 'fins', 'burn_time', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(StageUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageDeleteView(DeleteView):
    model = Stage
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("stage_list")
