from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import PropellantMix
from ..forms import PropellantMixForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PropellantMixListView(ListView):
    model = PropellantMix
    template_name = "catalog/propellant_mix_list.html"
    paginate_by = 20
    context_object_name = "propellant_mix_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PropellantMixListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PropellantMixListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PropellantMixListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PropellantMixListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PropellantMixListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PropellantMixListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PropellantMixListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PropellantMixListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PropellantMixListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PropellantMixListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PropellantMixListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PropellantMixListView, self).get_template_names()


class PropellantMixDetailView(DetailView):
    model = PropellantMix
    template_name = "catalog/propellant_mix_detail.html"
    context_object_name = "propellant_mix"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PropellantMixDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PropellantMixDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PropellantMixDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PropellantMixDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PropellantMixDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PropellantMixDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PropellantMixDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PropellantMixDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PropellantMixDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PropellantMixDetailView, self).get_template_names()


class PropellantMixCreateView(CreateView):
    model = PropellantMix
    form_class = PropellantMixForm
    # fields = ['abbreviation', 'hypergolic', 'specific_impulse', 'specific_impulse_sl', 'characteristic_velocity', 'optimum_ratio', 'combustion_temp', 'description', 'sources']
    template_name = "catalog/propellant_mix_create.html"
    success_url = reverse_lazy("propellant_mix_list")

    def __init__(self, **kwargs):
        return super(PropellantMixCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PropellantMixCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PropellantMixCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PropellantMixCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PropellantMixCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PropellantMixCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PropellantMixCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PropellantMixCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PropellantMixCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PropellantMixCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PropellantMixCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PropellantMixCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PropellantMixCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("propellant_mix_detail", args=(self.object.pk,))


class PropellantMixUpdateView(UpdateView):
    model = PropellantMix
    form_class = PropellantMixForm
    # fields = ['abbreviation', 'hypergolic', 'specific_impulse', 'specific_impulse_sl', 'characteristic_velocity', 'optimum_ratio', 'combustion_temp', 'description', 'sources']
    template_name = "catalog/propellant_mix_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "propellant_mix"

    def __init__(self, **kwargs):
        return super(PropellantMixUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PropellantMixUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PropellantMixUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PropellantMixUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PropellantMixUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PropellantMixUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PropellantMixUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PropellantMixUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PropellantMixUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PropellantMixUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PropellantMixUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PropellantMixUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PropellantMixUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PropellantMixUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PropellantMixUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PropellantMixUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PropellantMixUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("propellant_mix_detail", args=(self.object.pk,))


class PropellantMixDeleteView(DeleteView):
    model = PropellantMix
    template_name = "catalog/propellant_mix_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "propellant_mix"

    def __init__(self, **kwargs):
        return super(PropellantMixDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PropellantMixDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PropellantMixDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PropellantMixDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PropellantMixDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PropellantMixDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PropellantMixDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PropellantMixDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PropellantMixDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PropellantMixDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PropellantMixDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("propellant_mix_list")
