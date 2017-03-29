from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Mission
from ..forms import MissionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class MissionListView(ListView):
    model = Mission
    template_name = "catalog/mission_list.html"
    paginate_by = 20
    context_object_name = "mission_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(MissionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(MissionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(MissionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(MissionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(MissionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(MissionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(MissionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(MissionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionListView, self).get_template_names()


class MissionDetailView(DetailView):
    model = Mission
    template_name = "catalog/mission_detail.html"
    context_object_name = "mission"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(MissionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MissionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionDetailView, self).get_template_names()


class MissionCreateView(CreateView):
    model = Mission
    form_class = MissionForm
    # fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration']
    template_name = "catalog/mission_create.html"
    success_url = reverse_lazy("mission_list")

    def __init__(self, **kwargs):
        return super(MissionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(MissionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MissionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(MissionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MissionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MissionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MissionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(MissionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MissionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MissionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(MissionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_detail", args=(self.object.pk,))


class MissionUpdateView(UpdateView):
    model = Mission
    form_class = MissionForm
    # fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration']
    template_name = "catalog/mission_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "mission"

    def __init__(self, **kwargs):
        return super(MissionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MissionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(MissionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MissionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MissionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MissionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(MissionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MissionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MissionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_detail", args=(self.object.pk,))


class MissionDeleteView(DeleteView):
    model = Mission
    template_name = "catalog/mission_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "mission"

    def __init__(self, **kwargs):
        return super(MissionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(MissionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(MissionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MissionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_list")
