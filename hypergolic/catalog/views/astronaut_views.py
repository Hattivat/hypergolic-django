from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Astronaut, CrewedMission
from catalog.forms import AstronautForm
from catalog.filters import AstronautFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AstronautListView(GenericListView):
    model = Astronaut
    f = AstronautFilter
    display_data = ('organization', 'nationality', 'birth_date')


class AstronautDetailView(DetailView):
    model = Astronaut
    template_name = "catalog/astronaut_detail.html"


class AstronautCreateView(GenericCreateView):
    model = Astronaut
    form_class = AstronautForm
    success_url = reverse_lazy("astronaut_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(AstronautUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautUpdateView(UpdateView):
    model = Astronaut
    form_class = AstronautForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(AstronautUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautDeleteView(DeleteView):
    model = Astronaut
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("astronaut_list")
