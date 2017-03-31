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
    context_object_name = "engine"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(EngineDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EngineDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EngineDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EngineDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(EngineDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(EngineDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(EngineDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EngineDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EngineDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EngineDetailView, self).get_template_names()


class EngineCreateView(GenericCreateView):
    model = Engine
    form_class = EngineForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'application', 'propellants', 'mixture_ratio', 'cycle', 'specific_impulse_vac', 'specific_impulse_sl', 'thrust_sl', 'thrust_vac', 'twr', 'chamber_pressure', 'combustion_chambers', 'rated_burn_time', 'nozzle_ratio', 'nozzle_shape', 'nozzle_material', 'cooling_method', 'injector_type', 'coefficient_of_thrust_vac', 'coefficient_of_thrust_sl', 'ignition_method', 'restart_capability', 'num_restarts', 'throttle_range_min', 'throttle_range_max', 'illustration']
    template_name = "catalog/engine_create.html"
    success_url = reverse_lazy("engine_list")

    def __init__(self, **kwargs):
        return super(EngineCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(EngineCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EngineCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EngineCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(EngineCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EngineCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EngineCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EngineCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(EngineCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EngineCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EngineCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(EngineCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EngineCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineUpdateView(UpdateView):
    model = Engine
    form_class = EngineForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'application', 'propellants', 'mixture_ratio', 'cycle', 'specific_impulse_vac', 'specific_impulse_sl', 'thrust_sl', 'thrust_vac', 'twr', 'chamber_pressure', 'combustion_chambers', 'rated_burn_time', 'nozzle_ratio', 'nozzle_shape', 'nozzle_material', 'cooling_method', 'injector_type', 'coefficient_of_thrust_vac', 'coefficient_of_thrust_sl', 'ignition_method', 'restart_capability', 'num_restarts', 'throttle_range_min', 'throttle_range_max', 'illustration']
    template_name = "catalog/engine_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "engine"

    def __init__(self, **kwargs):
        return super(EngineUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EngineUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EngineUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EngineUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EngineUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(EngineUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(EngineUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(EngineUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EngineUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EngineUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EngineUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(EngineUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EngineUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EngineUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EngineUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EngineUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EngineUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineDeleteView(DeleteView):
    model = Engine
    template_name = "catalog/engine_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "engine"

    def __init__(self, **kwargs):
        return super(EngineDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EngineDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(EngineDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(EngineDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EngineDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(EngineDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(EngineDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(EngineDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EngineDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EngineDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EngineDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("engine_list")
