from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import GuidanceSystem
from ..forms import GuidanceSystemForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class GuidanceSystemListView(ListView):
    model = GuidanceSystem
    template_name = "catalog/guidance_system_list.html"
    paginate_by = 20
    context_object_name = "guidance_system_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(GuidanceSystemListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GuidanceSystemListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GuidanceSystemListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GuidanceSystemListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GuidanceSystemListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GuidanceSystemListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GuidanceSystemListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GuidanceSystemListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GuidanceSystemListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GuidanceSystemListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GuidanceSystemListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GuidanceSystemListView, self).get_template_names()


class GuidanceSystemDetailView(DetailView):
    model = GuidanceSystem
    template_name = "catalog/guidance_system_detail.html"
    context_object_name = "guidance_system"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(GuidanceSystemDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GuidanceSystemDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GuidanceSystemDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GuidanceSystemDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GuidanceSystemDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GuidanceSystemDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GuidanceSystemDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GuidanceSystemDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GuidanceSystemDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GuidanceSystemDetailView, self).get_template_names()


class GuidanceSystemCreateView(CreateView):
    model = GuidanceSystem
    form_class = GuidanceSystemForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/guidance_system_create.html"
    success_url = reverse_lazy("guidance_system_list")

    def __init__(self, **kwargs):
        return super(GuidanceSystemCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GuidanceSystemCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GuidanceSystemCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GuidanceSystemCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GuidanceSystemCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GuidanceSystemCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GuidanceSystemCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GuidanceSystemCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(GuidanceSystemCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GuidanceSystemCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GuidanceSystemCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GuidanceSystemCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GuidanceSystemCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("guidance_system_detail", args=(self.object.pk,))


class GuidanceSystemUpdateView(UpdateView):
    model = GuidanceSystem
    form_class = GuidanceSystemForm
    # fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
    template_name = "catalog/guidance_system_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "guidance_system"

    def __init__(self, **kwargs):
        return super(GuidanceSystemUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GuidanceSystemUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GuidanceSystemUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GuidanceSystemUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GuidanceSystemUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GuidanceSystemUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GuidanceSystemUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GuidanceSystemUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GuidanceSystemUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GuidanceSystemUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GuidanceSystemUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(GuidanceSystemUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GuidanceSystemUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GuidanceSystemUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GuidanceSystemUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GuidanceSystemUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GuidanceSystemUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("guidance_system_detail", args=(self.object.pk,))


class GuidanceSystemDeleteView(DeleteView):
    model = GuidanceSystem
    template_name = "catalog/guidance_system_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "guidance_system"

    def __init__(self, **kwargs):
        return super(GuidanceSystemDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GuidanceSystemDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GuidanceSystemDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GuidanceSystemDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GuidanceSystemDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GuidanceSystemDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GuidanceSystemDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GuidanceSystemDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GuidanceSystemDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GuidanceSystemDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GuidanceSystemDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("guidance_system_list")
