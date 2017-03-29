from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import LifeSupportType
from ..forms import LifeSupportTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class LifeSupportTypeListView(ListView):
    model = LifeSupportType
    template_name = "catalog/life_support_type_list.html"
    paginate_by = 20
    context_object_name = "life_support_type_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LifeSupportTypeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LifeSupportTypeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LifeSupportTypeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LifeSupportTypeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LifeSupportTypeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LifeSupportTypeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LifeSupportTypeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LifeSupportTypeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LifeSupportTypeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LifeSupportTypeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LifeSupportTypeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LifeSupportTypeListView, self).get_template_names()


class LifeSupportTypeDetailView(DetailView):
    model = LifeSupportType
    template_name = "catalog/life_support_type_detail.html"
    context_object_name = "life_support_type"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LifeSupportTypeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LifeSupportTypeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LifeSupportTypeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LifeSupportTypeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LifeSupportTypeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LifeSupportTypeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LifeSupportTypeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LifeSupportTypeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LifeSupportTypeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LifeSupportTypeDetailView, self).get_template_names()


class LifeSupportTypeCreateView(CreateView):
    model = LifeSupportType
    form_class = LifeSupportTypeForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/life_support_type_create.html"
    success_url = reverse_lazy("life_support_type_list")

    def __init__(self, **kwargs):
        return super(LifeSupportTypeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LifeSupportTypeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LifeSupportTypeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LifeSupportTypeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LifeSupportTypeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LifeSupportTypeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LifeSupportTypeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LifeSupportTypeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LifeSupportTypeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LifeSupportTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LifeSupportTypeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LifeSupportTypeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LifeSupportTypeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("life_support_type_detail", args=(self.object.pk,))


class LifeSupportTypeUpdateView(UpdateView):
    model = LifeSupportType
    form_class = LifeSupportTypeForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/life_support_type_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "life_support_type"

    def __init__(self, **kwargs):
        return super(LifeSupportTypeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LifeSupportTypeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LifeSupportTypeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LifeSupportTypeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LifeSupportTypeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LifeSupportTypeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LifeSupportTypeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LifeSupportTypeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LifeSupportTypeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LifeSupportTypeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LifeSupportTypeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LifeSupportTypeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LifeSupportTypeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LifeSupportTypeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LifeSupportTypeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LifeSupportTypeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LifeSupportTypeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("life_support_type_detail", args=(self.object.pk,))


class LifeSupportTypeDeleteView(DeleteView):
    model = LifeSupportType
    template_name = "catalog/life_support_type_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "life_support_type"

    def __init__(self, **kwargs):
        return super(LifeSupportTypeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LifeSupportTypeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LifeSupportTypeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LifeSupportTypeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LifeSupportTypeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LifeSupportTypeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LifeSupportTypeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LifeSupportTypeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LifeSupportTypeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LifeSupportTypeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LifeSupportTypeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("life_support_type_list")
