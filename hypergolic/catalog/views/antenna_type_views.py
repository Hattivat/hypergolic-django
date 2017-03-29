from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AntennaType
from ..forms import AntennaTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AntennaTypeListView(ListView):
    model = AntennaType
    template_name = "catalog/antenna_type_list.html"
    paginate_by = 20
    context_object_name = "antenna_type_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AntennaTypeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AntennaTypeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AntennaTypeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AntennaTypeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AntennaTypeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AntennaTypeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AntennaTypeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AntennaTypeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AntennaTypeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AntennaTypeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AntennaTypeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AntennaTypeListView, self).get_template_names()


class AntennaTypeDetailView(DetailView):
    model = AntennaType
    template_name = "catalog/antenna_type_detail.html"
    context_object_name = "antenna_type"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AntennaTypeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AntennaTypeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AntennaTypeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AntennaTypeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AntennaTypeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AntennaTypeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AntennaTypeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AntennaTypeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AntennaTypeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AntennaTypeDetailView, self).get_template_names()


class AntennaTypeCreateView(CreateView):
    model = AntennaType
    form_class = AntennaTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/antenna_type_create.html"
    success_url = reverse_lazy("antenna_type_list")

    def __init__(self, **kwargs):
        return super(AntennaTypeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AntennaTypeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AntennaTypeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AntennaTypeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AntennaTypeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AntennaTypeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AntennaTypeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AntennaTypeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AntennaTypeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AntennaTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AntennaTypeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AntennaTypeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AntennaTypeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("antenna_type_detail", args=(self.object.pk,))


class AntennaTypeUpdateView(UpdateView):
    model = AntennaType
    form_class = AntennaTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/antenna_type_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "antenna_type"

    def __init__(self, **kwargs):
        return super(AntennaTypeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AntennaTypeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AntennaTypeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AntennaTypeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AntennaTypeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AntennaTypeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AntennaTypeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AntennaTypeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AntennaTypeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AntennaTypeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AntennaTypeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AntennaTypeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AntennaTypeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AntennaTypeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AntennaTypeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AntennaTypeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AntennaTypeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("antenna_type_detail", args=(self.object.pk,))


class AntennaTypeDeleteView(DeleteView):
    model = AntennaType
    template_name = "catalog/antenna_type_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "antenna_type"

    def __init__(self, **kwargs):
        return super(AntennaTypeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AntennaTypeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AntennaTypeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AntennaTypeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AntennaTypeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AntennaTypeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AntennaTypeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AntennaTypeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AntennaTypeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AntennaTypeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AntennaTypeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("antenna_type_list")
