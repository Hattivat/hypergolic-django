from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Stage
from ..forms import StageForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StageListView(ListView):
    model = Stage
    template_name = "catalog/stage_list.html"
    paginate_by = 20
    context_object_name = "stage_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StageListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StageListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StageListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StageListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StageListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StageListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StageListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StageListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StageListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageListView, self).get_template_names()


class StageDetailView(DetailView):
    model = Stage
    template_name = "catalog/stage_detail.html"
    context_object_name = "stage"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StageDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StageDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StageDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageDetailView, self).get_template_names()


class StageCreateView(CreateView):
    model = Stage
    form_class = StageForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'stage_role', 'dry_weight', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'main_gimbal_yaw_min', 'main_gimbal_yaw_max', 'main_gimbal_pitch_min', 'main_gimbal_pitch_max', 'aux_engine', 'num_aux_engines', 'aux_gimbal_yaw_min', 'aux_gimbal_yaw_max', 'aux_gimbal_pitch_min', 'aux_gimbal_pitch_max', 'tank_type', 'tank_material', 'fins', 'burn_time', 'illustration']
    template_name = "catalog/stage_create.html"
    success_url = reverse_lazy("stage_list")

    def __init__(self, **kwargs):
        return super(StageCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StageCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StageCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StageCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StageCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StageCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StageCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StageCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StageCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StageCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageUpdateView(UpdateView):
    model = Stage
    form_class = StageForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'stage_role', 'dry_weight', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'main_gimbal_yaw_min', 'main_gimbal_yaw_max', 'main_gimbal_pitch_min', 'main_gimbal_pitch_max', 'aux_engine', 'num_aux_engines', 'aux_gimbal_yaw_min', 'aux_gimbal_yaw_max', 'aux_gimbal_pitch_min', 'aux_gimbal_pitch_max', 'tank_type', 'tank_material', 'fins', 'burn_time', 'illustration']
    template_name = "catalog/stage_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "stage"

    def __init__(self, **kwargs):
        return super(StageUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StageUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StageUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StageUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StageUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StageUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StageUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StageUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StageUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageDeleteView(DeleteView):
    model = Stage
    template_name = "catalog/stage_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "stage"

    def __init__(self, **kwargs):
        return super(StageDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StageDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StageDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StageDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StageDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_list")
