from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Rocket
from ..forms import RocketForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RocketListView(ListView):
    model = Rocket
    template_name = "catalog/rocket_list.html"
    paginate_by = 20
    context_object_name = "rocket_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RocketListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RocketListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RocketListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RocketListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RocketListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RocketListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RocketListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RocketListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketListView, self).get_template_names()


class RocketDetailView(DetailView):
    model = Rocket
    template_name = "catalog/rocket_detail.html"
    context_object_name = "rocket"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RocketDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RocketDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketDetailView, self).get_template_names()


class RocketCreateView(CreateView):
    model = Rocket
    form_class = RocketForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'series', 'dry_weight', 'fueled_weight', 'guidance_system', 'fairing_height', 'fairing_width', 'num_flights', 'failures', 'illustration']
    template_name = "catalog/rocket_create.html"
    success_url = reverse_lazy("rocket_list")

    def __init__(self, **kwargs):
        return super(RocketCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RocketCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RocketCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RocketCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RocketCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RocketCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RocketCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RocketCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RocketCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RocketCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RocketCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_detail", args=(self.object.pk,))


class RocketUpdateView(UpdateView):
    model = Rocket
    form_class = RocketForm
    # fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'series', 'dry_weight', 'fueled_weight', 'guidance_system', 'fairing_height', 'fairing_width', 'num_flights', 'failures', 'illustration']
    template_name = "catalog/rocket_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rocket"

    def __init__(self, **kwargs):
        return super(RocketUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RocketUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RocketUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RocketUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RocketUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RocketUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RocketUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RocketUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RocketUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_detail", args=(self.object.pk,))


class RocketDeleteView(DeleteView):
    model = Rocket
    template_name = "catalog/rocket_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rocket"

    def __init__(self, **kwargs):
        return super(RocketDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RocketDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RocketDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RocketDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_list")
