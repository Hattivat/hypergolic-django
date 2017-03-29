from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import MissionTarget
from ..forms import MissionTargetForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class MissionTargetListView(ListView):
    model = MissionTarget
    template_name = "catalog/mission_target_list.html"
    paginate_by = 20
    context_object_name = "mission_target_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(MissionTargetListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionTargetListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionTargetListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(MissionTargetListView, self).get_queryset()

    def get_allow_empty(self):
        return super(MissionTargetListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(MissionTargetListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(MissionTargetListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(MissionTargetListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(MissionTargetListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(MissionTargetListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionTargetListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionTargetListView, self).get_template_names()


class MissionTargetDetailView(DetailView):
    model = MissionTarget
    template_name = "catalog/mission_target_detail.html"
    context_object_name = "mission_target"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(MissionTargetDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionTargetDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionTargetDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionTargetDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionTargetDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionTargetDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MissionTargetDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionTargetDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionTargetDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionTargetDetailView, self).get_template_names()


class MissionTargetCreateView(CreateView):
    model = MissionTarget
    form_class = MissionTargetForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/mission_target_create.html"
    success_url = reverse_lazy("mission_target_list")

    def __init__(self, **kwargs):
        return super(MissionTargetCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(MissionTargetCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionTargetCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MissionTargetCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(MissionTargetCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MissionTargetCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MissionTargetCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MissionTargetCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(MissionTargetCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MissionTargetCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MissionTargetCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(MissionTargetCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionTargetCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_target_detail", args=(self.object.pk,))


class MissionTargetUpdateView(UpdateView):
    model = MissionTarget
    form_class = MissionTargetForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/mission_target_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "mission_target"

    def __init__(self, **kwargs):
        return super(MissionTargetUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionTargetUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MissionTargetUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MissionTargetUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionTargetUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionTargetUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionTargetUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(MissionTargetUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MissionTargetUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MissionTargetUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MissionTargetUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(MissionTargetUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MissionTargetUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MissionTargetUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionTargetUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionTargetUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionTargetUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_target_detail", args=(self.object.pk,))


class MissionTargetDeleteView(DeleteView):
    model = MissionTarget
    template_name = "catalog/mission_target_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "mission_target"

    def __init__(self, **kwargs):
        return super(MissionTargetDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MissionTargetDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(MissionTargetDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(MissionTargetDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MissionTargetDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(MissionTargetDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(MissionTargetDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MissionTargetDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MissionTargetDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MissionTargetDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MissionTargetDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("mission_target_list")
