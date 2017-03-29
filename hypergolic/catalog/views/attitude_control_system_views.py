from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AttitudeControlSystem
from ..forms import AttitudeControlSystemForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AttitudeControlSystemListView(ListView):
    model = AttitudeControlSystem
    template_name = "catalog/attitude_control_system_list.html"
    paginate_by = 20
    context_object_name = "attitude_control_system_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AttitudeControlSystemListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttitudeControlSystemListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttitudeControlSystemListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AttitudeControlSystemListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AttitudeControlSystemListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AttitudeControlSystemListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AttitudeControlSystemListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AttitudeControlSystemListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AttitudeControlSystemListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AttitudeControlSystemListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AttitudeControlSystemListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttitudeControlSystemListView, self).get_template_names()


class AttitudeControlSystemDetailView(DetailView):
    model = AttitudeControlSystem
    template_name = "catalog/attitude_control_system_detail.html"
    context_object_name = "attitude_control_system"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AttitudeControlSystemDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttitudeControlSystemDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttitudeControlSystemDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttitudeControlSystemDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttitudeControlSystemDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AttitudeControlSystemDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AttitudeControlSystemDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttitudeControlSystemDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttitudeControlSystemDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttitudeControlSystemDetailView, self).get_template_names()


class AttitudeControlSystemCreateView(CreateView):
    model = AttitudeControlSystem
    form_class = AttitudeControlSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/attitude_control_system_create.html"
    success_url = reverse_lazy("attitude_control_system_list")

    def __init__(self, **kwargs):
        return super(AttitudeControlSystemCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AttitudeControlSystemCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttitudeControlSystemCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AttitudeControlSystemCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AttitudeControlSystemCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AttitudeControlSystemCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AttitudeControlSystemCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AttitudeControlSystemCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AttitudeControlSystemCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AttitudeControlSystemCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AttitudeControlSystemCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AttitudeControlSystemCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttitudeControlSystemCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("attitude_control_system_detail", args=(self.object.pk,))


class AttitudeControlSystemUpdateView(UpdateView):
    model = AttitudeControlSystem
    form_class = AttitudeControlSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/attitude_control_system_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "attitude_control_system"

    def __init__(self, **kwargs):
        return super(AttitudeControlSystemUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttitudeControlSystemUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttitudeControlSystemUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AttitudeControlSystemUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttitudeControlSystemUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttitudeControlSystemUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AttitudeControlSystemUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AttitudeControlSystemUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AttitudeControlSystemUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AttitudeControlSystemUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AttitudeControlSystemUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AttitudeControlSystemUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AttitudeControlSystemUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AttitudeControlSystemUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttitudeControlSystemUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttitudeControlSystemUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttitudeControlSystemUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("attitude_control_system_detail", args=(self.object.pk,))


class AttitudeControlSystemDeleteView(DeleteView):
    model = AttitudeControlSystem
    template_name = "catalog/attitude_control_system_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "attitude_control_system"

    def __init__(self, **kwargs):
        return super(AttitudeControlSystemDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttitudeControlSystemDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AttitudeControlSystemDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AttitudeControlSystemDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttitudeControlSystemDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttitudeControlSystemDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AttitudeControlSystemDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AttitudeControlSystemDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttitudeControlSystemDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttitudeControlSystemDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttitudeControlSystemDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("attitude_control_system_list")
