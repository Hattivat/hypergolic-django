from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import LandingSolution
from ..forms import LandingSolutionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class LandingSolutionListView(ListView):
    model = LandingSolution
    template_name = "catalog/landing_solution_list.html"
    paginate_by = 20
    context_object_name = "landing_solution_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LandingSolutionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LandingSolutionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LandingSolutionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LandingSolutionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LandingSolutionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LandingSolutionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LandingSolutionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LandingSolutionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LandingSolutionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LandingSolutionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LandingSolutionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LandingSolutionListView, self).get_template_names()


class LandingSolutionDetailView(DetailView):
    model = LandingSolution
    template_name = "catalog/landing_solution_detail.html"
    context_object_name = "landing_solution"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LandingSolutionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LandingSolutionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LandingSolutionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LandingSolutionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LandingSolutionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LandingSolutionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LandingSolutionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LandingSolutionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LandingSolutionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LandingSolutionDetailView, self).get_template_names()


class LandingSolutionCreateView(CreateView):
    model = LandingSolution
    form_class = LandingSolutionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/landing_solution_create.html"
    success_url = reverse_lazy("landing_solution_list")

    def __init__(self, **kwargs):
        return super(LandingSolutionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LandingSolutionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LandingSolutionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LandingSolutionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LandingSolutionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LandingSolutionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LandingSolutionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LandingSolutionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LandingSolutionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LandingSolutionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LandingSolutionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LandingSolutionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LandingSolutionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("landing_solution_detail", args=(self.object.pk,))


class LandingSolutionUpdateView(UpdateView):
    model = LandingSolution
    form_class = LandingSolutionForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/landing_solution_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "landing_solution"

    def __init__(self, **kwargs):
        return super(LandingSolutionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LandingSolutionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LandingSolutionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LandingSolutionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LandingSolutionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LandingSolutionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LandingSolutionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LandingSolutionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LandingSolutionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LandingSolutionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LandingSolutionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LandingSolutionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LandingSolutionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LandingSolutionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LandingSolutionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LandingSolutionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LandingSolutionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("landing_solution_detail", args=(self.object.pk,))


class LandingSolutionDeleteView(DeleteView):
    model = LandingSolution
    template_name = "catalog/landing_solution_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "landing_solution"

    def __init__(self, **kwargs):
        return super(LandingSolutionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LandingSolutionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LandingSolutionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LandingSolutionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LandingSolutionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LandingSolutionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LandingSolutionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LandingSolutionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LandingSolutionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LandingSolutionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LandingSolutionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("landing_solution_list")
