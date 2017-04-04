from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import RocketSeries
from ..forms import RocketSeriesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class RocketSeriesListView(GenericListView):
    model = RocketSeries
    display_data = ('description', 'illustration')


class RocketSeriesDetailView(DetailView):
    model = RocketSeries
    template_name = "catalog/rocket_series_detail.html"


class RocketSeriesCreateView(GenericCreateView):
    model = RocketSeries
    form_class = RocketSeriesForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("rocket_series_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(RocketSeriesCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("rocket_series_detail", args=(self.object.pk,))


class RocketSeriesUpdateView(UpdateView):
    model = RocketSeries
    form_class = RocketSeriesForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(RocketSeriesUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("rocket_series_detail", args=(self.object.pk,))


class RocketSeriesDeleteView(DeleteView):
    model = RocketSeries
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("rocket_series_list")
