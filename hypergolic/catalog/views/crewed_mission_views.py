from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import CrewedMission
from catalog.forms import CrewedMissionForm
from catalog.filters import CrewedMissionFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class CrewedMissionListView(GenericListView):
    model = CrewedMission
    f = CrewedMissionFilter
    display_data = ('country', 'organization', 'print_crew', 'launch_date',
                    'launch_facility', 'launch_vehicle', 'spacecraft',
                    'print_targets')


class CrewedMissionDetailView(DetailView):
    model = CrewedMission
    template_name = "catalog/crewed_mission_detail.html"


class CrewedMissionCreateView(GenericCreateView):
    model = CrewedMission
    form_class = CrewedMissionForm
    success_url = reverse_lazy("crewed_mission_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(CrewedMissionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_mission_detail", args=(self.object.pk,))


class CrewedMissionUpdateView(UpdateView):
    model = CrewedMission
    form_class = CrewedMissionForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(CrewedMissionUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_mission_detail", args=(self.object.pk,))


class CrewedMissionDeleteView(DeleteView):
    model = CrewedMission
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("crewed_mission_list")
