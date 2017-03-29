from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Cooling
from ..forms import CoolingForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CoolingListView(ListView):
    model = Cooling
    template_name = "catalog/cooling_list.html"
    paginate_by = 20
    context_object_name = "cooling_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CoolingListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoolingListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CoolingListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CoolingListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CoolingListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CoolingListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CoolingListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CoolingListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CoolingListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CoolingListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CoolingListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoolingListView, self).get_template_names()


class CoolingDetailView(DetailView):
    model = Cooling
    template_name = "catalog/cooling_detail.html"
    context_object_name = "cooling"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CoolingDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoolingDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CoolingDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CoolingDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CoolingDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CoolingDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CoolingDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CoolingDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CoolingDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoolingDetailView, self).get_template_names()


class CoolingCreateView(CreateView):
    model = Cooling
    form_class = CoolingForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/cooling_create.html"
    success_url = reverse_lazy("cooling_list")

    def __init__(self, **kwargs):
        return super(CoolingCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CoolingCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CoolingCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CoolingCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CoolingCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CoolingCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CoolingCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CoolingCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CoolingCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CoolingCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CoolingCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CoolingCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoolingCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("cooling_detail", args=(self.object.pk,))


class CoolingUpdateView(UpdateView):
    model = Cooling
    form_class = CoolingForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/cooling_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "cooling"

    def __init__(self, **kwargs):
        return super(CoolingUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoolingUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CoolingUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CoolingUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CoolingUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CoolingUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CoolingUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CoolingUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CoolingUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CoolingUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CoolingUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CoolingUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CoolingUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CoolingUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CoolingUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CoolingUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoolingUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("cooling_detail", args=(self.object.pk,))


class CoolingDeleteView(DeleteView):
    model = Cooling
    template_name = "catalog/cooling_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "cooling"

    def __init__(self, **kwargs):
        return super(CoolingDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoolingDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CoolingDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CoolingDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CoolingDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CoolingDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CoolingDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CoolingDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CoolingDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CoolingDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoolingDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("cooling_list")
