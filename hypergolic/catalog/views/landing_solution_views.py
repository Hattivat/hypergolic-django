from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import LandingSolution
from ..forms import LandingSolutionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class LandingSolutionListView(GenericListView):
    model = LandingSolution
    display_data = ('description', 'illustration')


class LandingSolutionDetailView(DetailView):
    model = LandingSolution
    template_name = "catalog/generic_detail.html"


class LandingSolutionCreateView(GenericCreateView):
    model = LandingSolution
    form_class = LandingSolutionForm
    success_url = reverse_lazy("landing_solution_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(LandingSolutionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("landing_solution_detail", args=(self.object.pk,))


class LandingSolutionUpdateView(UpdateView):
    model = LandingSolution
    form_class = LandingSolutionForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(LandingSolutionUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("landing_solution_detail", args=(self.object.pk,))


class LandingSolutionDeleteView(DeleteView):
    model = LandingSolution
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("landing_solution_list")
