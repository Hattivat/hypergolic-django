from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import HeatshieldMaterial
from ..forms import HeatshieldMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class HeatshieldMaterialListView(ListView):
    model = HeatshieldMaterial
    template_name = "catalog/heatshield_material_list.html"
    paginate_by = 20
    context_object_name = "heatshield_material_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HeatshieldMaterialListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HeatshieldMaterialListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HeatshieldMaterialListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HeatshieldMaterialListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HeatshieldMaterialListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HeatshieldMaterialListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HeatshieldMaterialListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HeatshieldMaterialListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HeatshieldMaterialListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HeatshieldMaterialListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HeatshieldMaterialListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HeatshieldMaterialListView, self).get_template_names()


class HeatshieldMaterialDetailView(DetailView):
    model = HeatshieldMaterial
    template_name = "catalog/heatshield_material_detail.html"
    context_object_name = "heatshield_material"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(HeatshieldMaterialDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HeatshieldMaterialDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HeatshieldMaterialDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HeatshieldMaterialDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(HeatshieldMaterialDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(HeatshieldMaterialDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HeatshieldMaterialDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HeatshieldMaterialDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HeatshieldMaterialDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HeatshieldMaterialDetailView, self).get_template_names()


class HeatshieldMaterialCreateView(CreateView):
    model = HeatshieldMaterial
    form_class = HeatshieldMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration', 'chemical_formula']
    template_name = "catalog/heatshield_material_create.html"
    success_url = reverse_lazy("heatshield_material_list")

    def __init__(self, **kwargs):
        return super(HeatshieldMaterialCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(HeatshieldMaterialCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HeatshieldMaterialCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HeatshieldMaterialCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(HeatshieldMaterialCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HeatshieldMaterialCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HeatshieldMaterialCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HeatshieldMaterialCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(HeatshieldMaterialCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HeatshieldMaterialCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HeatshieldMaterialCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(HeatshieldMaterialCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HeatshieldMaterialCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("heatshield_material_detail", args=(self.object.pk,))


class HeatshieldMaterialUpdateView(UpdateView):
    model = HeatshieldMaterial
    form_class = HeatshieldMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration', 'chemical_formula']
    template_name = "catalog/heatshield_material_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "heatshield_material"

    def __init__(self, **kwargs):
        return super(HeatshieldMaterialUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HeatshieldMaterialUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HeatshieldMaterialUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HeatshieldMaterialUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HeatshieldMaterialUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(HeatshieldMaterialUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(HeatshieldMaterialUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(HeatshieldMaterialUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HeatshieldMaterialUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HeatshieldMaterialUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HeatshieldMaterialUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(HeatshieldMaterialUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HeatshieldMaterialUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HeatshieldMaterialUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HeatshieldMaterialUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HeatshieldMaterialUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HeatshieldMaterialUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("heatshield_material_detail", args=(self.object.pk,))


class HeatshieldMaterialDeleteView(DeleteView):
    model = HeatshieldMaterial
    template_name = "catalog/heatshield_material_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "heatshield_material"

    def __init__(self, **kwargs):
        return super(HeatshieldMaterialDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HeatshieldMaterialDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HeatshieldMaterialDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HeatshieldMaterialDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HeatshieldMaterialDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(HeatshieldMaterialDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(HeatshieldMaterialDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HeatshieldMaterialDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HeatshieldMaterialDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HeatshieldMaterialDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HeatshieldMaterialDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("heatshield_material_list")
