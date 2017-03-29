from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import StageRole
from ..forms import StageRoleForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StageRoleListView(ListView):
    model = StageRole
    template_name = "catalog/stage_role_list.html"
    paginate_by = 20
    context_object_name = "stage_role_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StageRoleListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageRoleListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageRoleListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StageRoleListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StageRoleListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StageRoleListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StageRoleListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StageRoleListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StageRoleListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StageRoleListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StageRoleListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageRoleListView, self).get_template_names()


class StageRoleDetailView(DetailView):
    model = StageRole
    template_name = "catalog/stage_role_detail.html"
    context_object_name = "stage_role"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StageRoleDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageRoleDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageRoleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageRoleDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageRoleDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StageRoleDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StageRoleDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageRoleDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageRoleDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageRoleDetailView, self).get_template_names()


class StageRoleCreateView(CreateView):
    model = StageRole
    form_class = StageRoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/stage_role_create.html"
    success_url = reverse_lazy("stage_role_list")

    def __init__(self, **kwargs):
        return super(StageRoleCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StageRoleCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageRoleCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StageRoleCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StageRoleCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StageRoleCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StageRoleCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StageRoleCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StageRoleCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageRoleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StageRoleCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StageRoleCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageRoleCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_role_detail", args=(self.object.pk,))


class StageRoleUpdateView(UpdateView):
    model = StageRole
    form_class = StageRoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/stage_role_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "stage_role"

    def __init__(self, **kwargs):
        return super(StageRoleUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageRoleUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StageRoleUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StageRoleUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageRoleUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageRoleUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StageRoleUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StageRoleUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StageRoleUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StageRoleUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StageRoleUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StageRoleUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageRoleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StageRoleUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageRoleUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageRoleUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageRoleUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_role_detail", args=(self.object.pk,))


class StageRoleDeleteView(DeleteView):
    model = StageRole
    template_name = "catalog/stage_role_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "stage_role"

    def __init__(self, **kwargs):
        return super(StageRoleDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StageRoleDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StageRoleDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StageRoleDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StageRoleDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StageRoleDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StageRoleDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StageRoleDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StageRoleDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StageRoleDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StageRoleDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("stage_role_list")
