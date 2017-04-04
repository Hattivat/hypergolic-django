from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import MissionTarget
from ..forms import MissionTargetForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class MissionTargetListView(GenericListView):
    model = MissionTarget
    display_data = ('description', 'illustration')


class MissionTargetDetailView(DetailView):
    model = MissionTarget
    template_name = "catalog/generic_detail.html"


class MissionTargetCreateView(GenericCreateView):
    model = MissionTarget
    form_class = MissionTargetForm
    success_url = reverse_lazy("mission_target_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(MissionTargetCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("mission_target_detail", args=(self.object.pk,))


class MissionTargetUpdateView(UpdateView):
    model = MissionTarget
    form_class = MissionTargetForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(MissionTargetUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("mission_target_detail", args=(self.object.pk,))


class MissionTargetDeleteView(DeleteView):
    model = MissionTarget
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("mission_target_list")
