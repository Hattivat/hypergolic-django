from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import Compound
from catalog.forms import CompoundForm
from catalog.filters import CompoundFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class CompoundListView(GenericListView):
    model = Compound
    f = CompoundFilter
    display_data = ('role', 'chemical_formula', 'also_known_as',
                    'density')


class CompoundDetailView(DetailView):
    model = Compound
    template_name = "catalog/compound_detail.html"


class CompoundCreateView(GenericCreateView):
    model = Compound
    form_class = CompoundForm
    # fields = ['name', 'description', 'sources', 'role', 'chemical_formula',
    # 'also_known_as', 'variety_of', 'density', 'melting_point',
    # 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
    success_url = reverse_lazy("compound_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
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
        obj.modifier = self.request.user
        obj.save()
        return super(CompoundUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("compound_detail", args=(self.object.pk,))


class CompoundDeleteView(DeleteView):
    model = Compound
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("compound_list")
