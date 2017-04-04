from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import AttitudeControlSystem
from ..forms import AttitudeControlSystemForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class AttitudeControlSystemListView(GenericListView):
    model = AttitudeControlSystem
    display_data = ('description', 'illustration')


class AttitudeControlSystemDetailView(DetailView):
    model = AttitudeControlSystem
    template_name = "catalog/generic_detail.html"


class AttitudeControlSystemCreateView(GenericCreateView):
    model = AttitudeControlSystem
    form_class = AttitudeControlSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("attitude_control_system_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(AttitudeControlSystemCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("attitude_control_system_detail", args=(self.object.pk,))


class AttitudeControlSystemUpdateView(UpdateView):
    model = AttitudeControlSystem
    form_class = AttitudeControlSystemForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(AttitudeControlSystemUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("attitude_control_system_detail", args=(self.object.pk,))


class AttitudeControlSystemDeleteView(DeleteView):
    model = AttitudeControlSystem
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("attitude_control_system_list")
