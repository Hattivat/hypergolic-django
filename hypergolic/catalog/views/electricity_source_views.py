from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import ElectricitySource
from ..forms import ElectricitySourceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ElectricitySourceListView(ListView):
    model = ElectricitySource
    template_name = "catalog/electricity_source_list.html"
    paginate_by = 20
    context_object_name = "electricity_source_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ElectricitySourceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ElectricitySourceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ElectricitySourceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ElectricitySourceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ElectricitySourceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ElectricitySourceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ElectricitySourceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ElectricitySourceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ElectricitySourceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ElectricitySourceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ElectricitySourceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ElectricitySourceListView, self).get_template_names()


class ElectricitySourceDetailView(DetailView):
    model = ElectricitySource
    template_name = "catalog/electricity_source_detail.html"
    context_object_name = "electricity_source"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ElectricitySourceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ElectricitySourceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ElectricitySourceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ElectricitySourceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ElectricitySourceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ElectricitySourceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ElectricitySourceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ElectricitySourceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ElectricitySourceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ElectricitySourceDetailView, self).get_template_names()


class ElectricitySourceCreateView(CreateView):
    model = ElectricitySource
    form_class = ElectricitySourceForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/electricity_source_create.html"
    success_url = reverse_lazy("electricity_source_list")

    def __init__(self, **kwargs):
        return super(ElectricitySourceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ElectricitySourceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ElectricitySourceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ElectricitySourceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ElectricitySourceCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ElectricitySourceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ElectricitySourceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ElectricitySourceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ElectricitySourceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ElectricitySourceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ElectricitySourceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ElectricitySourceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ElectricitySourceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("electricity_source_detail", args=(self.object.pk,))


class ElectricitySourceUpdateView(UpdateView):
    model = ElectricitySource
    form_class = ElectricitySourceForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/electricity_source_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "electricity_source"

    def __init__(self, **kwargs):
        return super(ElectricitySourceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ElectricitySourceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ElectricitySourceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ElectricitySourceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ElectricitySourceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ElectricitySourceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ElectricitySourceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ElectricitySourceUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ElectricitySourceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ElectricitySourceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ElectricitySourceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ElectricitySourceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ElectricitySourceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ElectricitySourceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ElectricitySourceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ElectricitySourceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ElectricitySourceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("electricity_source_detail", args=(self.object.pk,))


class ElectricitySourceDeleteView(DeleteView):
    model = ElectricitySource
    template_name = "catalog/electricity_source_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "electricity_source"

    def __init__(self, **kwargs):
        return super(ElectricitySourceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ElectricitySourceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ElectricitySourceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ElectricitySourceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ElectricitySourceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ElectricitySourceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ElectricitySourceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ElectricitySourceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ElectricitySourceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ElectricitySourceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ElectricitySourceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("electricity_source_list")
