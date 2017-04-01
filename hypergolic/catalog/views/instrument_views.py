from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Instrument
from ..forms import InstrumentForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class InstrumentListView(GenericListView):
    model = Instrument
    display_data = ('energy_consumption', 'description', 'illustration')


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "catalog/electric_detail.html"


class InstrumentCreateView(GenericCreateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("instrument_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstrumentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("instrument_detail", args=(self.object.pk,))


class InstrumentUpdateView(UpdateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstrumentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("instrument_detail", args=(self.object.pk,))


class InstrumentDeleteView(DeleteView):
    model = Instrument
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("instrument_list")
