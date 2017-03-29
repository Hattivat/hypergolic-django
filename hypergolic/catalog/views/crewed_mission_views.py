from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CrewedMission
from ..forms import CrewedMissionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CrewedMissionListView(ListView):
    model = CrewedMission
    template_name = "catalog/crewed_mission_list.html"
    paginate_by = 20
    context_object_name = "crewed_mission_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CrewedMissionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CrewedMissionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CrewedMissionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CrewedMissionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CrewedMissionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CrewedMissionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CrewedMissionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CrewedMissionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CrewedMissionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CrewedMissionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CrewedMissionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CrewedMissionListView, self).get_template_names()


class CrewedMissionDetailView(DetailView):
    model = CrewedMission
    template_name = "catalog/crewed_mission_detail.html"
    context_object_name = "crewed_mission"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CrewedMissionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CrewedMissionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CrewedMissionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CrewedMissionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CrewedMissionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CrewedMissionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CrewedMissionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CrewedMissionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CrewedMissionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CrewedMissionDetailView, self).get_template_names()


class CrewedMissionCreateView(CreateView):
    model = CrewedMission
    form_class = CrewedMissionForm
    # fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration', 'mission_ptr', 'landing_site']
    template_name = "catalog/crewed_mission_create.html"
    success_url = reverse_lazy("crewed_mission_list")

    def __init__(self, **kwargs):
        return super(CrewedMissionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CrewedMissionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CrewedMissionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CrewedMissionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CrewedMissionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CrewedMissionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CrewedMissionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CrewedMissionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CrewedMissionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CrewedMissionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CrewedMissionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CrewedMissionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CrewedMissionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("crewed_mission_detail", args=(self.object.pk,))


class CrewedMissionUpdateView(UpdateView):
    model = CrewedMission
    form_class = CrewedMissionForm
    # fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration', 'mission_ptr', 'landing_site']
    template_name = "catalog/crewed_mission_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "crewed_mission"

    def __init__(self, **kwargs):
        return super(CrewedMissionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CrewedMissionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CrewedMissionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CrewedMissionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CrewedMissionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CrewedMissionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CrewedMissionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CrewedMissionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CrewedMissionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CrewedMissionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CrewedMissionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CrewedMissionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CrewedMissionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CrewedMissionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CrewedMissionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CrewedMissionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CrewedMissionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("crewed_mission_detail", args=(self.object.pk,))


class CrewedMissionDeleteView(DeleteView):
    model = CrewedMission
    template_name = "catalog/crewed_mission_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "crewed_mission"

    def __init__(self, **kwargs):
        return super(CrewedMissionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CrewedMissionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CrewedMissionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CrewedMissionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CrewedMissionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CrewedMissionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CrewedMissionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CrewedMissionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CrewedMissionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CrewedMissionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CrewedMissionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("crewed_mission_list")
