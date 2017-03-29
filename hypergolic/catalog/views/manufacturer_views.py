from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Manufacturer
from ..forms import ManufacturerForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "catalog/manufacturer_list.html"
    paginate_by = 20
    context_object_name = "manufacturer_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ManufacturerListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ManufacturerListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ManufacturerListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ManufacturerListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ManufacturerListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ManufacturerListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ManufacturerListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ManufacturerListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ManufacturerListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ManufacturerListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ManufacturerListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ManufacturerListView, self).get_template_names()


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "catalog/manufacturer_detail.html"
    context_object_name = "manufacturer"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ManufacturerDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ManufacturerDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ManufacturerDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ManufacturerDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ManufacturerDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ManufacturerDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ManufacturerDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ManufacturerDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ManufacturerDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ManufacturerDetailView, self).get_template_names()


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    # fields = ['name', 'description', 'sources', 'native_name', 'country', 'established', 'active', 'defunct', 'successor', 'headquarters', 'website', 'illustration']
    template_name = "catalog/manufacturer_create.html"
    success_url = reverse_lazy("manufacturer_list")

    def __init__(self, **kwargs):
        return super(ManufacturerCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ManufacturerCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ManufacturerCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ManufacturerCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ManufacturerCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ManufacturerCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ManufacturerCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ManufacturerCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ManufacturerCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ManufacturerCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ManufacturerCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ManufacturerCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ManufacturerCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("manufacturer_detail", args=(self.object.pk,))


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    # fields = ['name', 'description', 'sources', 'native_name', 'country', 'established', 'active', 'defunct', 'successor', 'headquarters', 'website', 'illustration']
    template_name = "catalog/manufacturer_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "manufacturer"

    def __init__(self, **kwargs):
        return super(ManufacturerUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ManufacturerUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ManufacturerUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ManufacturerUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ManufacturerUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ManufacturerUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ManufacturerUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ManufacturerUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ManufacturerUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ManufacturerUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ManufacturerUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ManufacturerUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ManufacturerUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ManufacturerUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ManufacturerUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ManufacturerUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ManufacturerUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("manufacturer_detail", args=(self.object.pk,))


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = "catalog/manufacturer_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "manufacturer"

    def __init__(self, **kwargs):
        return super(ManufacturerDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ManufacturerDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ManufacturerDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ManufacturerDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ManufacturerDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ManufacturerDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ManufacturerDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ManufacturerDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ManufacturerDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ManufacturerDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ManufacturerDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("manufacturer_list")
