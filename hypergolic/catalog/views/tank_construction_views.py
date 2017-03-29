from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import TankConstruction
from ..forms import TankConstructionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class TankConstructionListView(ListView):
    model = TankConstruction
    template_name = "catalog/tank_construction_list.html"
    paginate_by = 20
    context_object_name = "tank_construction_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(TankConstructionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankConstructionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankConstructionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(TankConstructionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(TankConstructionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(TankConstructionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(TankConstructionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(TankConstructionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(TankConstructionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(TankConstructionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(TankConstructionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankConstructionListView, self).get_template_names()


class TankConstructionDetailView(DetailView):
    model = TankConstruction
    template_name = "catalog/tank_construction_detail.html"
    context_object_name = "tank_construction"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(TankConstructionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankConstructionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankConstructionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankConstructionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankConstructionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(TankConstructionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TankConstructionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankConstructionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankConstructionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankConstructionDetailView, self).get_template_names()


class TankConstructionCreateView(CreateView):
    model = TankConstruction
    form_class = TankConstructionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/tank_construction_create.html"
    success_url = reverse_lazy("tank_construction_list")

    def __init__(self, **kwargs):
        return super(TankConstructionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(TankConstructionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankConstructionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TankConstructionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(TankConstructionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TankConstructionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TankConstructionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TankConstructionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(TankConstructionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankConstructionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TankConstructionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(TankConstructionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankConstructionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_construction_detail", args=(self.object.pk,))


class TankConstructionUpdateView(UpdateView):
    model = TankConstruction
    form_class = TankConstructionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/tank_construction_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tank_construction"

    def __init__(self, **kwargs):
        return super(TankConstructionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankConstructionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TankConstructionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TankConstructionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankConstructionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankConstructionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(TankConstructionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(TankConstructionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TankConstructionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TankConstructionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TankConstructionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(TankConstructionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TankConstructionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TankConstructionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankConstructionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankConstructionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankConstructionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_construction_detail", args=(self.object.pk,))


class TankConstructionDeleteView(DeleteView):
    model = TankConstruction
    template_name = "catalog/tank_construction_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tank_construction"

    def __init__(self, **kwargs):
        return super(TankConstructionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TankConstructionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(TankConstructionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TankConstructionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TankConstructionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(TankConstructionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(TankConstructionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TankConstructionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TankConstructionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TankConstructionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TankConstructionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("tank_construction_list")
