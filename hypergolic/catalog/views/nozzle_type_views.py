from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import NozzleType
from ..forms import NozzleTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class NozzleTypeListView(ListView):
    model = NozzleType
    template_name = "catalog/nozzle_type_list.html"
    paginate_by = 20
    context_object_name = "nozzle_type_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(NozzleTypeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleTypeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleTypeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(NozzleTypeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(NozzleTypeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(NozzleTypeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(NozzleTypeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(NozzleTypeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(NozzleTypeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(NozzleTypeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleTypeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleTypeListView, self).get_template_names()


class NozzleTypeDetailView(DetailView):
    model = NozzleType
    template_name = "catalog/nozzle_type_detail.html"
    context_object_name = "nozzle_type"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(NozzleTypeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleTypeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleTypeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleTypeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleTypeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleTypeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NozzleTypeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleTypeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleTypeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleTypeDetailView, self).get_template_names()


class NozzleTypeCreateView(CreateView):
    model = NozzleType
    form_class = NozzleTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/nozzle_type_create.html"
    success_url = reverse_lazy("nozzle_type_list")

    def __init__(self, **kwargs):
        return super(NozzleTypeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(NozzleTypeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleTypeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NozzleTypeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(NozzleTypeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NozzleTypeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NozzleTypeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NozzleTypeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(NozzleTypeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NozzleTypeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleTypeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleTypeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_type_detail", args=(self.object.pk,))


class NozzleTypeUpdateView(UpdateView):
    model = NozzleType
    form_class = NozzleTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/nozzle_type_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nozzle_type"

    def __init__(self, **kwargs):
        return super(NozzleTypeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleTypeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleTypeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NozzleTypeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleTypeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleTypeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleTypeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(NozzleTypeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NozzleTypeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NozzleTypeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NozzleTypeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(NozzleTypeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleTypeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NozzleTypeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleTypeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleTypeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleTypeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_type_detail", args=(self.object.pk,))


class NozzleTypeDeleteView(DeleteView):
    model = NozzleType
    template_name = "catalog/nozzle_type_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nozzle_type"

    def __init__(self, **kwargs):
        return super(NozzleTypeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleTypeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(NozzleTypeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(NozzleTypeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleTypeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleTypeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleTypeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NozzleTypeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleTypeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleTypeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleTypeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_type_list")
