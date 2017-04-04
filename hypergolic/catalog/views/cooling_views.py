from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Cooling
from ..forms import CoolingForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class CoolingListView(GenericListView):
    model = Cooling
    display_data = ('description', 'illustration')


class CoolingDetailView(DetailView):
    model = Cooling
    template_name = "catalog/generic_detail.html"


class CoolingCreateView(GenericCreateView):
    model = Cooling
    form_class = CoolingForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("cooling_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(CoolingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("cooling_detail", args=(self.object.pk,))


class CoolingUpdateView(UpdateView):
    model = Cooling
    form_class = CoolingForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(CoolingUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("cooling_detail", args=(self.object.pk,))


class CoolingDeleteView(DeleteView):
    model = Cooling
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("cooling_list")
