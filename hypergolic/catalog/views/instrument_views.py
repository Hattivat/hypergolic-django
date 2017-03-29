from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Instrument
from ..forms import InstrumentForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class InstrumentListView(ListView):
    model = Instrument
    template_name = "catalog/instrument_list.html"
    paginate_by = 20
    context_object_name = "instrument_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(InstrumentListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstrumentListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstrumentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(InstrumentListView, self).get_queryset()

    def get_allow_empty(self):
        return super(InstrumentListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(InstrumentListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(InstrumentListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(InstrumentListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(InstrumentListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(InstrumentListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(InstrumentListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstrumentListView, self).get_template_names()


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "catalog/instrument_detail.html"
    context_object_name = "instrument"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(InstrumentDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstrumentDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstrumentDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstrumentDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstrumentDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(InstrumentDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InstrumentDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstrumentDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstrumentDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstrumentDetailView, self).get_template_names()


class InstrumentCreateView(CreateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/instrument_create.html"
    success_url = reverse_lazy("instrument_list")

    def __init__(self, **kwargs):
        return super(InstrumentCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(InstrumentCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstrumentCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InstrumentCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(InstrumentCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InstrumentCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InstrumentCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InstrumentCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(InstrumentCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstrumentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InstrumentCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(InstrumentCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstrumentCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("instrument_detail", args=(self.object.pk,))


class InstrumentUpdateView(UpdateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/instrument_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "instrument"

    def __init__(self, **kwargs):
        return super(InstrumentUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstrumentUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstrumentUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InstrumentUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstrumentUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstrumentUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(InstrumentUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(InstrumentUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InstrumentUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InstrumentUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InstrumentUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(InstrumentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstrumentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InstrumentUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstrumentUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstrumentUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstrumentUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("instrument_detail", args=(self.object.pk,))


class InstrumentDeleteView(DeleteView):
    model = Instrument
    template_name = "catalog/instrument_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "instrument"

    def __init__(self, **kwargs):
        return super(InstrumentDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstrumentDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(InstrumentDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(InstrumentDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstrumentDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstrumentDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(InstrumentDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InstrumentDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstrumentDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstrumentDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstrumentDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("instrument_list")
