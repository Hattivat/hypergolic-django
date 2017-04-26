from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Engine
from catalog.forms import EngineForm
from catalog.filters import EngineFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class EngineListView(GenericListView):
    model = Engine
    f = EngineFilter
    display_data = ('country', 'developed', 'application',
                    'propellants', 'cycle', 'specific_impulse_vac',
                    'thrust_vac', 'twr')


class EngineDetailView(DetailView):
    model = Engine
    template_name = "catalog/engine_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(EngineDetailView, self).get_context_data(**kwargs)
        return ret


class EngineCreateView(GenericCreateView):
    model = Engine
    form_class = EngineForm
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("engine_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(EngineCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineUpdateView(UpdateView):
    model = Engine
    form_class = EngineForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(EngineUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("engine_detail", args=(self.object.pk,))


class EngineDeleteView(DeleteView):
    model = Engine
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("engine_list")
