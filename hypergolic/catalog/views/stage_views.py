from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Stage
from catalog.forms import StageForm
from catalog.filters import StageFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StageListView(GenericListView):
    model = Stage
    f = StageFilter
    display_data = ('country', 'developed', 'fueled_weight', 'stage_role',
                    'main_engine', 'aux_engine', 'country', 'manufacturer',
                    'tank_type')


class StageDetailView(DetailView):
    model = Stage
    template_name = "catalog/stage_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(StageDetailView, self).get_context_data(**kwargs)
        return ret


class StageCreateView(GenericCreateView):
    model = Stage
    form_class = StageForm
    template_name = "catalog/generic_create.html"
    success_url = reverse_lazy("stage_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(StageCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageUpdateView(UpdateView):
    model = Stage
    form_class = StageForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(StageUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_detail", args=(self.object.pk,))


class StageDeleteView(DeleteView):
    model = Stage
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("stage_list")
