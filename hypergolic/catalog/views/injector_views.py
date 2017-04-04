from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Injector
from ..forms import InjectorForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class InjectorListView(GenericListView):
    model = Injector
    display_data = ('description', 'illustration')


class InjectorDetailView(DetailView):
    model = Injector
    template_name = "catalog/generic_detail.html"


class InjectorCreateView(GenericCreateView):
    model = Injector
    form_class = InjectorForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("injector_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(InjectorCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("injector_detail", args=(self.object.pk,))


class InjectorUpdateView(UpdateView):
    model = Injector
    form_class = InjectorForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(InjectorUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("injector_detail", args=(self.object.pk,))


class InjectorDeleteView(DeleteView):
    model = Injector
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("injector_list")
