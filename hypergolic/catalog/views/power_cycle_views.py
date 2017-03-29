from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import PowerCycle
from ..forms import PowerCycleForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PowerCycleListView(ListView):
    model = PowerCycle
    template_name = "catalog/power_cycle_list.html"
    paginate_by = 20
    context_object_name = "power_cycle_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PowerCycleListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PowerCycleListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PowerCycleListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PowerCycleListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PowerCycleListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PowerCycleListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PowerCycleListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PowerCycleListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PowerCycleListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PowerCycleListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PowerCycleListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PowerCycleListView, self).get_template_names()


class PowerCycleDetailView(DetailView):
    model = PowerCycle
    template_name = "catalog/power_cycle_detail.html"
    context_object_name = "power_cycle"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PowerCycleDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PowerCycleDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PowerCycleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PowerCycleDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PowerCycleDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PowerCycleDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PowerCycleDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PowerCycleDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PowerCycleDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PowerCycleDetailView, self).get_template_names()


class PowerCycleCreateView(CreateView):
    model = PowerCycle
    form_class = PowerCycleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/power_cycle_create.html"
    success_url = reverse_lazy("power_cycle_list")

    def __init__(self, **kwargs):
        return super(PowerCycleCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PowerCycleCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PowerCycleCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PowerCycleCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PowerCycleCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PowerCycleCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PowerCycleCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PowerCycleCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PowerCycleCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PowerCycleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PowerCycleCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PowerCycleCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PowerCycleCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("power_cycle_detail", args=(self.object.pk,))


class PowerCycleUpdateView(UpdateView):
    model = PowerCycle
    form_class = PowerCycleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/power_cycle_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "power_cycle"

    def __init__(self, **kwargs):
        return super(PowerCycleUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PowerCycleUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PowerCycleUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PowerCycleUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PowerCycleUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PowerCycleUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PowerCycleUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PowerCycleUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PowerCycleUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PowerCycleUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PowerCycleUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PowerCycleUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PowerCycleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PowerCycleUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PowerCycleUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PowerCycleUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PowerCycleUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("power_cycle_detail", args=(self.object.pk,))


class PowerCycleDeleteView(DeleteView):
    model = PowerCycle
    template_name = "catalog/power_cycle_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "power_cycle"

    def __init__(self, **kwargs):
        return super(PowerCycleDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PowerCycleDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PowerCycleDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PowerCycleDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PowerCycleDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PowerCycleDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PowerCycleDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PowerCycleDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PowerCycleDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PowerCycleDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PowerCycleDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("power_cycle_list")
