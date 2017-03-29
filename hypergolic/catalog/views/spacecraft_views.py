from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Spacecraft
from ..forms import SpacecraftForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SpacecraftListView(ListView):
    model = Spacecraft
    template_name = "catalog/spacecraft_list.html"
    paginate_by = 20
    context_object_name = "spacecraft_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SpacecraftListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SpacecraftListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SpacecraftListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SpacecraftListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SpacecraftListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SpacecraftListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SpacecraftListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SpacecraftListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SpacecraftListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SpacecraftListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SpacecraftListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SpacecraftListView, self).get_template_names()


class SpacecraftDetailView(DetailView):
    model = Spacecraft
    template_name = "catalog/spacecraft_detail.html"
    context_object_name = "spacecraft"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SpacecraftDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SpacecraftDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SpacecraftDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SpacecraftDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SpacecraftDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SpacecraftDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SpacecraftDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SpacecraftDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SpacecraftDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SpacecraftDetailView, self).get_template_names()


class SpacecraftCreateView(CreateView):
    model = Spacecraft
    form_class = SpacecraftForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system', 'battery_capacity', 'electricity_source', 'power_generation', 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield', 'landing_solution', 'num_flights', 'failures', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines', 'tank_type', 'tank_material', 'illustration']
    template_name = "catalog/spacecraft_create.html"
    success_url = reverse_lazy("spacecraft_list")

    def __init__(self, **kwargs):
        return super(SpacecraftCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SpacecraftCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SpacecraftCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SpacecraftCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SpacecraftCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SpacecraftCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SpacecraftCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SpacecraftCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SpacecraftCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SpacecraftCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SpacecraftCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SpacecraftCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SpacecraftCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("spacecraft_detail", args=(self.object.pk,))


class SpacecraftUpdateView(UpdateView):
    model = Spacecraft
    form_class = SpacecraftForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system', 'battery_capacity', 'electricity_source', 'power_generation', 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield', 'landing_solution', 'num_flights', 'failures', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines', 'tank_type', 'tank_material', 'illustration']
    template_name = "catalog/spacecraft_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "spacecraft"

    def __init__(self, **kwargs):
        return super(SpacecraftUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SpacecraftUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SpacecraftUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SpacecraftUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SpacecraftUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SpacecraftUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SpacecraftUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SpacecraftUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SpacecraftUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SpacecraftUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SpacecraftUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SpacecraftUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SpacecraftUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SpacecraftUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SpacecraftUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SpacecraftUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SpacecraftUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("spacecraft_detail", args=(self.object.pk,))


class SpacecraftDeleteView(DeleteView):
    model = Spacecraft
    template_name = "catalog/spacecraft_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "spacecraft"

    def __init__(self, **kwargs):
        return super(SpacecraftDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SpacecraftDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SpacecraftDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SpacecraftDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SpacecraftDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SpacecraftDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SpacecraftDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SpacecraftDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SpacecraftDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SpacecraftDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SpacecraftDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("spacecraft_list")
