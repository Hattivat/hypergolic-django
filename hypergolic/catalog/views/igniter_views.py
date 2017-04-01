from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Igniter
from ..forms import IgniterForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class IgniterListView(GenericListView):
    model = Igniter
    display_data = ('description', 'illustration')


class IgniterDetailView(DetailView):
    model = Igniter
    template_name = "catalog/generic_detail.html"


class IgniterCreateView(GenericCreateView):
    model = Igniter
    form_class = IgniterForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("igniter_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(IgniterCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("igniter_detail", args=(self.object.pk,))


class IgniterUpdateView(UpdateView):
    model = Igniter
    form_class = IgniterForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(IgniterUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("igniter_detail", args=(self.object.pk,))


class IgniterDeleteView(DeleteView):
    model = Igniter
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("igniter_list")
