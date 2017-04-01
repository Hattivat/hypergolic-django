from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import LifeSupportType
from ..forms import LifeSupportTypeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class LifeSupportTypeListView(GenericListView):
    model = LifeSupportType
    display_data = ('energy_consumption', 'description', 'illustration')


class LifeSupportTypeDetailView(DetailView):
    model = LifeSupportType
    template_name = "catalog/electric_detail.html"


class LifeSupportTypeCreateView(GenericCreateView):
    model = LifeSupportType
    form_class = LifeSupportTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("life_support_type_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LifeSupportTypeCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("life_support_type_detail", args=(self.object.pk,))


class LifeSupportTypeUpdateView(UpdateView):
    model = LifeSupportType
    form_class = LifeSupportTypeForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LifeSupportTypeUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("life_support_type_detail", args=(self.object.pk,))


class LifeSupportTypeDeleteView(DeleteView):
    model = LifeSupportType
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("life_support_type_list")
