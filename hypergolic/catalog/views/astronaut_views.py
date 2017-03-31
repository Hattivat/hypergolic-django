from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Astronaut, CrewedMission
from ..forms import AstronautForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AstronautListView(GenericListView):
    model = Astronaut
    display_data = ('organization', 'nationality', 'birth_date')


class AstronautDetailView(DetailView):
    model = Astronaut
    template_name = "catalog/astronaut_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AstronautDetailView, self).get_context_data(**kwargs)
        missions = CrewedMission.objects.filter(crew__contains=self.object.pk)
        context['missions'] = missions
        context['num_missions'] = len(missions)
        return context


class AstronautCreateView(GenericCreateView):
    model = Astronaut
    form_class = AstronautForm
    # fields = ['first_name', 'middle_names', 'last_name', 'nationality',
    # 'organization', 'birth_date', 'birth_place', 'death_date', 'biography',
    # 'sources', 'picture']
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("astronaut_list")

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautUpdateView(UpdateView):
    model = Astronaut
    form_class = AstronautForm
    # fields = ['first_name', 'middle_names', 'last_name', 'nationality',
    # 'organization', 'birth_date', 'birth_place', 'death_date', 'biography',
    # 'sources', 'picture']
    template_name = "catalog/generic_update.html"
    initial = {}

    def get_success_url(self):
        return reverse("astronaut_detail", args=(self.object.pk,))


class AstronautDeleteView(DeleteView):
    model = Astronaut
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("astronaut_list")
