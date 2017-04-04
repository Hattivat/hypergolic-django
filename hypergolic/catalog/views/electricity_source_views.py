from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import ElectricitySource
from ..forms import ElectricitySourceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class ElectricitySourceListView(GenericListView):
    model = ElectricitySource
    display_data = ('description', 'illustration')


class ElectricitySourceDetailView(DetailView):
    model = ElectricitySource
    template_name = "catalog/generic_detail.html"


class ElectricitySourceCreateView(GenericCreateView):
    model = ElectricitySource
    form_class = ElectricitySourceForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("electricity_source_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(ElectricitySourceCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("electricity_source_detail", args=(self.object.pk,))


class ElectricitySourceUpdateView(UpdateView):
    model = ElectricitySource
    form_class = ElectricitySourceForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(ElectricitySourceUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("electricity_source_detail", args=(self.object.pk,))


class ElectricitySourceDeleteView(DeleteView):
    model = ElectricitySource
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("electricity_source_list")
