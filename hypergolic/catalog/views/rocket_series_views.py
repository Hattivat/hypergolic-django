from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RocketSeries
from ..forms import RocketSeriesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RocketSeriesListView(ListView):
    model = RocketSeries
    template_name = "catalog/rocket_series_list.html"
    paginate_by = 20
    context_object_name = "rocket_series_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RocketSeriesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketSeriesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketSeriesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RocketSeriesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RocketSeriesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RocketSeriesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RocketSeriesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RocketSeriesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RocketSeriesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RocketSeriesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketSeriesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketSeriesListView, self).get_template_names()


class RocketSeriesDetailView(DetailView):
    model = RocketSeries
    template_name = "catalog/rocket_series_detail.html"
    context_object_name = "rocket_series"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RocketSeriesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketSeriesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketSeriesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketSeriesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketSeriesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketSeriesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RocketSeriesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketSeriesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketSeriesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketSeriesDetailView, self).get_template_names()


class RocketSeriesCreateView(CreateView):
    model = RocketSeries
    form_class = RocketSeriesForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/rocket_series_create.html"
    success_url = reverse_lazy("rocket_series_list")

    def __init__(self, **kwargs):
        return super(RocketSeriesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RocketSeriesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketSeriesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RocketSeriesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RocketSeriesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RocketSeriesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RocketSeriesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RocketSeriesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RocketSeriesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RocketSeriesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RocketSeriesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RocketSeriesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketSeriesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_series_detail", args=(self.object.pk,))


class RocketSeriesUpdateView(UpdateView):
    model = RocketSeries
    form_class = RocketSeriesForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/rocket_series_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rocket_series"

    def __init__(self, **kwargs):
        return super(RocketSeriesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketSeriesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RocketSeriesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RocketSeriesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketSeriesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketSeriesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketSeriesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RocketSeriesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RocketSeriesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RocketSeriesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RocketSeriesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RocketSeriesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RocketSeriesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RocketSeriesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketSeriesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketSeriesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketSeriesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_series_detail", args=(self.object.pk,))


class RocketSeriesDeleteView(DeleteView):
    model = RocketSeries
    template_name = "catalog/rocket_series_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rocket_series"

    def __init__(self, **kwargs):
        return super(RocketSeriesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RocketSeriesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RocketSeriesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RocketSeriesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RocketSeriesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RocketSeriesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RocketSeriesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RocketSeriesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RocketSeriesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RocketSeriesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RocketSeriesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("rocket_series_list")
