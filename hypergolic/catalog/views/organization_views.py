from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Organization
from ..forms import OrganizationForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class OrganizationListView(ListView):
    model = Organization
    template_name = "catalog/organization_list.html"
    paginate_by = 20
    context_object_name = "organization_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(OrganizationListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganizationListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganizationListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(OrganizationListView, self).get_queryset()

    def get_allow_empty(self):
        return super(OrganizationListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(OrganizationListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(OrganizationListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(OrganizationListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(OrganizationListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(OrganizationListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganizationListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganizationListView, self).get_template_names()


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "catalog/organization_detail.html"
    context_object_name = "organization"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(OrganizationDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganizationDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganizationDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganizationDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganizationDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganizationDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(OrganizationDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganizationDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganizationDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganizationDetailView, self).get_template_names()


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/organization_create.html"
    success_url = reverse_lazy("organization_list")

    def __init__(self, **kwargs):
        return super(OrganizationCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(OrganizationCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganizationCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(OrganizationCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(OrganizationCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(OrganizationCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(OrganizationCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(OrganizationCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(OrganizationCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(OrganizationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(OrganizationCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(OrganizationCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganizationCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("organization_detail", args=(self.object.pk,))


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/organization_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "organization"

    def __init__(self, **kwargs):
        return super(OrganizationUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganizationUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganizationUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(OrganizationUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganizationUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganizationUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganizationUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(OrganizationUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(OrganizationUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(OrganizationUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(OrganizationUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(OrganizationUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(OrganizationUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(OrganizationUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganizationUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganizationUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganizationUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("organization_detail", args=(self.object.pk,))


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "catalog/organization_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "organization"

    def __init__(self, **kwargs):
        return super(OrganizationDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganizationDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(OrganizationDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(OrganizationDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganizationDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganizationDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganizationDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(OrganizationDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganizationDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganizationDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganizationDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("organization_list")
