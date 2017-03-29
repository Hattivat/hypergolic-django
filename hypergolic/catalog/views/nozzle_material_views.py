from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import NozzleMaterial
from ..forms import NozzleMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class NozzleMaterialListView(ListView):
    model = NozzleMaterial
    template_name = "catalog/nozzle_material_list.html"
    paginate_by = 20
    context_object_name = "nozzle_material_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(NozzleMaterialListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleMaterialListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleMaterialListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(NozzleMaterialListView, self).get_queryset()

    def get_allow_empty(self):
        return super(NozzleMaterialListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(NozzleMaterialListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(NozzleMaterialListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(NozzleMaterialListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(NozzleMaterialListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(NozzleMaterialListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleMaterialListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleMaterialListView, self).get_template_names()


class NozzleMaterialDetailView(DetailView):
    model = NozzleMaterial
    template_name = "catalog/nozzle_material_detail.html"
    context_object_name = "nozzle_material"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(NozzleMaterialDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleMaterialDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleMaterialDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleMaterialDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleMaterialDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleMaterialDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NozzleMaterialDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleMaterialDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleMaterialDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleMaterialDetailView, self).get_template_names()


class NozzleMaterialCreateView(CreateView):
    model = NozzleMaterial
    form_class = NozzleMaterialForm
    # fields = ['name', 'description', 'sources', 'chemical_formula', 'illustration']
    template_name = "catalog/nozzle_material_create.html"
    success_url = reverse_lazy("nozzle_material_list")

    def __init__(self, **kwargs):
        return super(NozzleMaterialCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(NozzleMaterialCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleMaterialCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NozzleMaterialCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(NozzleMaterialCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NozzleMaterialCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NozzleMaterialCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NozzleMaterialCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(NozzleMaterialCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleMaterialCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NozzleMaterialCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleMaterialCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleMaterialCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_material_detail", args=(self.object.pk,))


class NozzleMaterialUpdateView(UpdateView):
    model = NozzleMaterial
    form_class = NozzleMaterialForm
    # fields = ['name', 'description', 'sources', 'chemical_formula', 'illustration']
    template_name = "catalog/nozzle_material_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nozzle_material"

    def __init__(self, **kwargs):
        return super(NozzleMaterialUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleMaterialUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NozzleMaterialUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NozzleMaterialUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleMaterialUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleMaterialUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleMaterialUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(NozzleMaterialUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NozzleMaterialUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NozzleMaterialUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NozzleMaterialUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(NozzleMaterialUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleMaterialUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NozzleMaterialUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleMaterialUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleMaterialUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleMaterialUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_material_detail", args=(self.object.pk,))


class NozzleMaterialDeleteView(DeleteView):
    model = NozzleMaterial
    template_name = "catalog/nozzle_material_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nozzle_material"

    def __init__(self, **kwargs):
        return super(NozzleMaterialDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NozzleMaterialDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(NozzleMaterialDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(NozzleMaterialDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NozzleMaterialDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(NozzleMaterialDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(NozzleMaterialDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NozzleMaterialDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NozzleMaterialDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NozzleMaterialDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NozzleMaterialDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("nozzle_material_list")
