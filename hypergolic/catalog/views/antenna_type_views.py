from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import AntennaType
from ..forms import AntennaTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class AntennaTypeListView(GenericListView):
    model = AntennaType
    display_data = ('description', 'illustration')


class AntennaTypeDetailView(DetailView):
    model = AntennaType
    template_name = "catalog/generic_detail.html"


class AntennaTypeCreateView(GenericCreateView):
    model = AntennaType
    form_class = AntennaTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("antenna_type_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(AntennaTypeCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("antenna_type_detail", args=(self.object.pk,))


class AntennaTypeUpdateView(UpdateView):
    model = AntennaType
    form_class = AntennaTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(AntennaTypeUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("antenna_type_detail", args=(self.object.pk,))


class AntennaTypeDeleteView(DeleteView):
    model = AntennaType
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("antenna_type_list")
