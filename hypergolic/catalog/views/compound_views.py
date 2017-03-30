from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import BasicListView, BasicCreateView
from ..models import Compound
from ..forms import CompoundForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404
from ..helpers import underscore


class CompoundListView(BasicListView):
    model = Compound
    template_name = "catalog/generic_list.html"
    display_data = ('name', 'role', 'chemical_formula', 'also_known_as',
                    'density')


class CompoundDetailView(DetailView):
    model = Compound
    template_name = "catalog/compound_detail.html"


class CompoundCreateView(BasicCreateView):
    model = Compound
    form_class = CompoundForm
    # fields = ['name', 'description', 'sources', 'role', 'chemical_formula',
    # 'also_known_as', 'variety_of', 'density', 'melting_point',
    # 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
    success_url = reverse_lazy("compound_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CompoundCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("compound_detail", args=(self.object.pk,))


class CompoundUpdateView(UpdateView):
    model = Compound
    form_class = CompoundForm
    # fields = ['name', 'description', 'sources', 'role', 'chemical_formula',
    # 'also_known_as', 'variety_of', 'density', 'melting_point',
    # 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CompoundUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("compound_detail", args=(self.object.pk,))


class CompoundDeleteView(DeleteView):
    model = Compound
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("compound_list")
