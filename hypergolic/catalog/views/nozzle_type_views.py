from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import NozzleType
from ..forms import NozzleTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class NozzleTypeListView(GenericListView):
    model = NozzleType
    display_data = ('description', 'illustration')


class NozzleTypeDetailView(DetailView):
    model = NozzleType
    template_name = "catalog/generic_detail.html"


class NozzleTypeCreateView(GenericCreateView):
    model = NozzleType
    form_class = NozzleTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("nozzle_type_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleTypeCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("nozzle_type_detail", args=(self.object.pk,))


class NozzleTypeUpdateView(UpdateView):
    model = NozzleType
    form_class = NozzleTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NozzleTypeUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("nozzle_type_detail", args=(self.object.pk,))


class NozzleTypeDeleteView(DeleteView):
    model = NozzleType
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("nozzle_type_list")
