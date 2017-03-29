from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Injector
from ..forms import InjectorForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class InjectorListView(ListView):
    model = Injector
    template_name = "catalog/injector_list.html"
    paginate_by = 20
    context_object_name = "injector_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(InjectorListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InjectorListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InjectorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(InjectorListView, self).get_queryset()

    def get_allow_empty(self):
        return super(InjectorListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(InjectorListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(InjectorListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(InjectorListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(InjectorListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(InjectorListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(InjectorListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InjectorListView, self).get_template_names()


class InjectorDetailView(DetailView):
    model = Injector
    template_name = "catalog/injector_detail.html"
    context_object_name = "injector"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(InjectorDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InjectorDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InjectorDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InjectorDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(InjectorDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(InjectorDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InjectorDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InjectorDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InjectorDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InjectorDetailView, self).get_template_names()


class InjectorCreateView(CreateView):
    model = Injector
    form_class = InjectorForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/injector_create.html"
    success_url = reverse_lazy("injector_list")

    def __init__(self, **kwargs):
        return super(InjectorCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(InjectorCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InjectorCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InjectorCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(InjectorCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InjectorCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InjectorCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InjectorCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(InjectorCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InjectorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InjectorCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(InjectorCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InjectorCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("injector_detail", args=(self.object.pk,))


class InjectorUpdateView(UpdateView):
    model = Injector
    form_class = InjectorForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/injector_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "injector"

    def __init__(self, **kwargs):
        return super(InjectorUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InjectorUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InjectorUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InjectorUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InjectorUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(InjectorUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(InjectorUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(InjectorUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InjectorUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InjectorUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InjectorUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(InjectorUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InjectorUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InjectorUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InjectorUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InjectorUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InjectorUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("injector_detail", args=(self.object.pk,))


class InjectorDeleteView(DeleteView):
    model = Injector
    template_name = "catalog/injector_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "injector"

    def __init__(self, **kwargs):
        return super(InjectorDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InjectorDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(InjectorDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(InjectorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InjectorDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(InjectorDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(InjectorDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InjectorDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InjectorDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InjectorDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InjectorDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("injector_list")