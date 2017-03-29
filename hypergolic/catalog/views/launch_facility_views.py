from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import LaunchFacility
from ..forms import LaunchFacilityForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class LaunchFacilityListView(ListView):
    model = LaunchFacility
    template_name = "catalog/launch_facility_list.html"
    paginate_by = 20
    context_object_name = "launch_facility_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LaunchFacilityListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LaunchFacilityListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LaunchFacilityListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LaunchFacilityListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LaunchFacilityListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LaunchFacilityListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LaunchFacilityListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LaunchFacilityListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LaunchFacilityListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LaunchFacilityListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LaunchFacilityListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LaunchFacilityListView, self).get_template_names()


class LaunchFacilityDetailView(DetailView):
    model = LaunchFacility
    template_name = "catalog/launch_facility_detail.html"
    context_object_name = "launch_facility"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LaunchFacilityDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LaunchFacilityDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LaunchFacilityDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LaunchFacilityDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LaunchFacilityDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LaunchFacilityDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LaunchFacilityDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LaunchFacilityDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LaunchFacilityDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LaunchFacilityDetailView, self).get_template_names()


class LaunchFacilityCreateView(CreateView):
    model = LaunchFacility
    form_class = LaunchFacilityForm
    # fields = ['name', 'description', 'sources', 'location', 'owning_country', 'latitude', 'longitude', 'elevation', 'illustration']
    template_name = "catalog/launch_facility_create.html"
    success_url = reverse_lazy("launch_facility_list")

    def __init__(self, **kwargs):
        return super(LaunchFacilityCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LaunchFacilityCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LaunchFacilityCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LaunchFacilityCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LaunchFacilityCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LaunchFacilityCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LaunchFacilityCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LaunchFacilityCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LaunchFacilityCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LaunchFacilityCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LaunchFacilityCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LaunchFacilityCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LaunchFacilityCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("launch_facility_detail", args=(self.object.pk,))


class LaunchFacilityUpdateView(UpdateView):
    model = LaunchFacility
    form_class = LaunchFacilityForm
    # fields = ['name', 'description', 'sources', 'location', 'owning_country', 'latitude', 'longitude', 'elevation', 'illustration']
    template_name = "catalog/launch_facility_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "launch_facility"

    def __init__(self, **kwargs):
        return super(LaunchFacilityUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LaunchFacilityUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LaunchFacilityUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LaunchFacilityUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LaunchFacilityUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LaunchFacilityUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LaunchFacilityUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LaunchFacilityUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LaunchFacilityUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LaunchFacilityUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LaunchFacilityUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LaunchFacilityUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LaunchFacilityUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LaunchFacilityUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LaunchFacilityUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LaunchFacilityUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LaunchFacilityUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("launch_facility_detail", args=(self.object.pk,))


class LaunchFacilityDeleteView(DeleteView):
    model = LaunchFacility
    template_name = "catalog/launch_facility_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "launch_facility"

    def __init__(self, **kwargs):
        return super(LaunchFacilityDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LaunchFacilityDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LaunchFacilityDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LaunchFacilityDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LaunchFacilityDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LaunchFacilityDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LaunchFacilityDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LaunchFacilityDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LaunchFacilityDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LaunchFacilityDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LaunchFacilityDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("launch_facility_list")
