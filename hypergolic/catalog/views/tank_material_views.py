from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import TankMaterial
from ..forms import TankMaterialForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class TankMaterialListView(ListView):
    model = TankMaterial
    template_name = "catalog/tank_material_list.html"
    paginate_by = 20
    context_object_name = "tank_material_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(TankMaterialListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankMaterialListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankMaterialListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(TankMaterialListView, self).get_queryset()

    def get_allow_empty(self):
        return super(TankMaterialListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(TankMaterialListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(TankMaterialListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(TankMaterialListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(TankMaterialListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(TankMaterialListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(TankMaterialListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankMaterialListView, self).get_template_names()


class TankMaterialDetailView(DetailView):
    model = TankMaterial
    template_name = "catalog/tank_material_detail.html"
    context_object_name = "tank_material"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(TankMaterialDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankMaterialDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankMaterialDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankMaterialDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankMaterialDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(TankMaterialDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TankMaterialDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankMaterialDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankMaterialDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankMaterialDetailView, self).get_template_names()


class TankMaterialCreateView(CreateView):
    model = TankMaterial
    form_class = TankMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/tank_material_create.html"
    success_url = reverse_lazy("tank_material_list")

    def __init__(self, **kwargs):
        return super(TankMaterialCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(TankMaterialCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankMaterialCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TankMaterialCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(TankMaterialCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TankMaterialCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TankMaterialCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TankMaterialCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(TankMaterialCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankMaterialCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TankMaterialCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(TankMaterialCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankMaterialCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_material_detail", args=(self.object.pk,))


class TankMaterialUpdateView(UpdateView):
    model = TankMaterial
    form_class = TankMaterialForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/tank_material_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tank_material"

    def __init__(self, **kwargs):
        return super(TankMaterialUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankMaterialUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankMaterialUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TankMaterialUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankMaterialUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankMaterialUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(TankMaterialUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(TankMaterialUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TankMaterialUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TankMaterialUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TankMaterialUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(TankMaterialUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankMaterialUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TankMaterialUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankMaterialUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankMaterialUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankMaterialUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_material_detail", args=(self.object.pk,))


class TankMaterialDeleteView(DeleteView):
    model = TankMaterial
    template_name = "catalog/tank_material_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tank_material"

    def __init__(self, **kwargs):
        return super(TankMaterialDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankMaterialDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(TankMaterialDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TankMaterialDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankMaterialDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankMaterialDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(TankMaterialDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TankMaterialDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankMaterialDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankMaterialDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankMaterialDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_material_list")
