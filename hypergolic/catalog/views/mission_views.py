from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Mission
from catalog.forms import MissionForm
from catalog.filters import MissionFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class MissionListView(GenericListView):
    model = Mission
    f = MissionFilter
    display_data = ('country', 'organization', 'launch_date',
                    'launch_facility', 'launch_vehicle', 'spacecraft',
                    'print_targets')


class MissionDetailView(DetailView):
    model = Mission
    template_name = "catalog/mission_detail.html"


class MissionCreateView(GenericCreateView):
    model = Mission
    form_class = MissionForm
    success_url = reverse_lazy("mission_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(MissionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("mission_detail", args=(self.object.pk,))


class MissionUpdateView(UpdateView):
    model = Mission
    form_class = MissionForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(MissionUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("mission_detail", args=(self.object.pk,))


class MissionDeleteView(DeleteView):
    model = Mission
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("mission_list")
