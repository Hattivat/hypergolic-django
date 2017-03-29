from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Igniter
from ..forms import IgniterForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class IgniterListView(ListView):
    model = Igniter
    template_name = "catalog/igniter_list.html"
    paginate_by = 20
    context_object_name = "igniter_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(IgniterListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(IgniterListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IgniterListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(IgniterListView, self).get_queryset()

    def get_allow_empty(self):
        return super(IgniterListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(IgniterListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(IgniterListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(IgniterListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(IgniterListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(IgniterListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(IgniterListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(IgniterListView, self).get_template_names()


class IgniterDetailView(DetailView):
    model = Igniter
    template_name = "catalog/igniter_detail.html"
    context_object_name = "igniter"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(IgniterDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(IgniterDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IgniterDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(IgniterDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(IgniterDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(IgniterDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(IgniterDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(IgniterDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(IgniterDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(IgniterDetailView, self).get_template_names()


class IgniterCreateView(CreateView):
    model = Igniter
    form_class = IgniterForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/igniter_create.html"
    success_url = reverse_lazy("igniter_list")

    def __init__(self, **kwargs):
        return super(IgniterCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(IgniterCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IgniterCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(IgniterCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(IgniterCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(IgniterCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(IgniterCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(IgniterCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(IgniterCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(IgniterCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(IgniterCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(IgniterCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(IgniterCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("igniter_detail", args=(self.object.pk,))


class IgniterUpdateView(UpdateView):
    model = Igniter
    form_class = IgniterForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/igniter_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "igniter"

    def __init__(self, **kwargs):
        return super(IgniterUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(IgniterUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IgniterUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(IgniterUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(IgniterUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(IgniterUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(IgniterUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(IgniterUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(IgniterUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(IgniterUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(IgniterUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(IgniterUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(IgniterUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(IgniterUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(IgniterUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(IgniterUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(IgniterUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("igniter_detail", args=(self.object.pk,))


class IgniterDeleteView(DeleteView):
    model = Igniter
    template_name = "catalog/igniter_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "igniter"

    def __init__(self, **kwargs):
        return super(IgniterDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(IgniterDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(IgniterDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(IgniterDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(IgniterDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(IgniterDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(IgniterDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(IgniterDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(IgniterDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(IgniterDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(IgniterDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("igniter_list")
