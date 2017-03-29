from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Compound
from ..forms import CompoundForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CompoundListView(ListView):
    model = Compound
    template_name = "catalog/compound_list.html"
    paginate_by = 20
    context_object_name = "compound_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CompoundListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CompoundListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CompoundListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CompoundListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CompoundListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CompoundListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CompoundListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CompoundListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CompoundListView, self).paginate_queryset(queryset,
                                                               page_size)

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True):
        return super(CompoundListView, self).get_paginator(queryset, per_page,
                                                           orphans=0,
                                                           allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CompoundListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CompoundListView, self).get_template_names()


class CompoundDetailView(DetailView):
    model = Compound
    template_name = "catalog/compound_detail.html"
    context_object_name = "compound"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CompoundDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CompoundDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CompoundDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CompoundDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CompoundDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CompoundDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CompoundDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CompoundDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CompoundDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CompoundDetailView, self).get_template_names()


class CompoundCreateView(CreateView):
    model = Compound
    form_class = CompoundForm
    # fields = ['name', 'description', 'sources', 'role', 'chemical_formula', 'also_known_as', 'variety_of', 'density', 'melting_point', 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
    template_name = "catalog/compound_create.html"
    success_url = reverse_lazy("compound_list")

    def __init__(self, **kwargs):
        return super(CompoundCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CompoundCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CompoundCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CompoundCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CompoundCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CompoundCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CompoundCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CompoundCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CompoundCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CompoundCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CompoundCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CompoundCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CompoundCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("compound_detail", args=(self.object.pk,))


class CompoundUpdateView(UpdateView):
    model = Compound
    form_class = CompoundForm
    # fields = ['name', 'description', 'sources', 'role', 'chemical_formula', 'also_known_as', 'variety_of', 'density', 'melting_point', 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
    template_name = "catalog/compound_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "compound"

    def __init__(self, **kwargs):
        return super(CompoundUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CompoundUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CompoundUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CompoundUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CompoundUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CompoundUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CompoundUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CompoundUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CompoundUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CompoundUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CompoundUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CompoundUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CompoundUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CompoundUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CompoundUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CompoundUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CompoundUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("compound_detail", args=(self.object.pk,))


class CompoundDeleteView(DeleteView):
    model = Compound
    template_name = "catalog/compound_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "compound"

    def __init__(self, **kwargs):
        return super(CompoundDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CompoundDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CompoundDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CompoundDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CompoundDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CompoundDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CompoundDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CompoundDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CompoundDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CompoundDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CompoundDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("compound_list")
