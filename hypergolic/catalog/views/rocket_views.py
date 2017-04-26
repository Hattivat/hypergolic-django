from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Rocket
from catalog.forms import RocketForm
from catalog.filters import RocketFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RocketListView(GenericListView):
    model = Rocket
    f = RocketFilter
    display_data = ('country', 'first_flight', 'num_stages',
                    'num_flights', 'failures')


class RocketDetailView(DetailView):
    model = Rocket
    template_name = "catalog/rocket_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(RocketDetailView, self).get_context_data(**kwargs)
        return ret


class RocketCreateView(GenericCreateView):
    model = Rocket
    form_class = RocketForm
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("rocket_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(RocketCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("rocket_detail", args=(self.object.pk,))


class RocketUpdateView(UpdateView):
    model = Rocket
    form_class = RocketForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(RocketUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("rocket_detail", args=(self.object.pk,))


class RocketDeleteView(DeleteView):
    model = Rocket
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("rocket_list")
