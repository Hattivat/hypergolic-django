from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import LaunchFacility
from catalog.forms import LaunchFacilityForm
from catalog.filters import LaunchFacilityFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class LaunchFacilityListView(GenericListView):
    model = LaunchFacility
    f = LaunchFacilityFilter
    display_data = ('location', 'owning_country', 'latitude', 'longitude',
                    'elevation')


class LaunchFacilityDetailView(DetailView):
    model = LaunchFacility
    template_name = "catalog/launch_facility_detail.html"


class LaunchFacilityCreateView(GenericCreateView):
    model = LaunchFacility
    form_class = LaunchFacilityForm
    success_url = reverse_lazy("launch_facility_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(LaunchFacilityCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("launch_facility_detail", args=(self.object.pk,))


class LaunchFacilityUpdateView(UpdateView):
    model = LaunchFacility
    form_class = LaunchFacilityForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(LaunchFacilityUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("launch_facility_detail", args=(self.object.pk,))


class LaunchFacilityDeleteView(DeleteView):
    model = LaunchFacility
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("launch_facility_list")
