from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Astronaut
from ..forms import AstronautForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AstronautListView(ListView):
    model = Astronaut
    template_name = "catalog/astronaut_list.html"
    paginate_by = 20
    context_object_name = "astronaut_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AstronautListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AstronautListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AstronautListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AstronautListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AstronautListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AstronautListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AstronautListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AstronautListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AstronautListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AstronautListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AstronautListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AstronautListView, self).get_template_names()


class AstronautDetailView(DetailView):
    model = Astronaut
    template_name = "catalog/astronaut_detail.html"
    context_object_name = "astronaut"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AstronautDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AstronautDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AstronautDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AstronautDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AstronautDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AstronautDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AstronautDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AstronautDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AstronautDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AstronautDetailView, self).get_template_names()


class AstronautCreateView(CreateView):
    model = Astronaut
    form_class = AstronautForm
    # fields = ['first_name', 'middle_names', 'last_name', 'nationality', 'organization', 'birth_date', 'birth_place', 'death_date', 'biography', 'sources', 'picture']
    template_name = "catalog/astronaut_create.html"
    success_url = reverse_lazy("astronaut_list")

    def __init__(self, **kwargs):
        return super(AstronautCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AstronautCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AstronautCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AstronautCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AstronautCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AstronautCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AstronautCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AstronautCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AstronautCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AstronautCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AstronautCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AstronautCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AstronautCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautUpdateView(UpdateView):
    model = Astronaut
    form_class = AstronautForm
    # fields = ['first_name', 'middle_names', 'last_name', 'nationality', 'organization', 'birth_date', 'birth_place', 'death_date', 'biography', 'sources', 'picture']
    template_name = "catalog/astronaut_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "astronaut"

    def __init__(self, **kwargs):
        return super(AstronautUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AstronautUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AstronautUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AstronautUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AstronautUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AstronautUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AstronautUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AstronautUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AstronautUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AstronautUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AstronautUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AstronautUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AstronautUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AstronautUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AstronautUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AstronautUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AstronautUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautDeleteView(DeleteView):
    model = Astronaut
    template_name = "catalog/astronaut_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "astronaut"

    def __init__(self, **kwargs):
        return super(AstronautDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AstronautDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AstronautDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AstronautDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AstronautDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AstronautDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AstronautDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AstronautDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AstronautDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AstronautDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AstronautDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("astronaut_list")
