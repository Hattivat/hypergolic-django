from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import CrewedSpacecraft
from catalog.forms import CrewedSpacecraftForm
from catalog.filters import CrewedSpacecraftFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CrewedSpacecraftListView(GenericListView):
    model = CrewedSpacecraft
    f = CrewedSpacecraftFilter
    display_data = ('country', 'first_flight', 'fueled_weight', 'manufacturer')


class CrewedSpacecraftDetailView(DetailView):
    model = CrewedSpacecraft
    template_name = "catalog/crewed_spacecraft_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(CrewedSpacecraftDetailView, self).get_context_data(**kwargs)
        return ret


class CrewedSpacecraftCreateView(GenericCreateView):
    model = CrewedSpacecraft
    form_class = CrewedSpacecraftForm
    success_url = reverse_lazy("crewed_spacecraft_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(CrewedSpacecraftCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_spacecraft_detail", args=(self.object.pk,))


class CrewedSpacecraftUpdateView(UpdateView):
    model = CrewedSpacecraft
    form_class = CrewedSpacecraftForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(CrewedSpacecraftUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("crewed_spacecraft_detail", args=(self.object.pk,))


class CrewedSpacecraftDeleteView(DeleteView):
    model = CrewedSpacecraft
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("crewed_spacecraft_list")
