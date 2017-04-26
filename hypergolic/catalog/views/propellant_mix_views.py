from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.views.base import GenericListView, GenericCreateView
from catalog.models import PropellantMix
from catalog.forms import PropellantMixForm
from catalog.filters import PropellantMixFilter
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class PropellantMixListView(GenericListView):
    model = PropellantMix
    f = PropellantMixFilter
    display_data = ('abbreviation', 'specific_impulse', 'hypergolic',
                    'optimum_ratio', 'combustion_temp')


class PropellantMixDetailView(DetailView):
    model = PropellantMix
    template_name = "catalog/propellant_mix_detail.html"

    def get_context_data(self, **kwargs):
        ret = super(PropellantMixDetailView, self).get_context_data(**kwargs)
        props = self.object.propellants.all()
        ret['fuels'] = props.filter(role=True)
        ret['oxidizers'] = props.filter(role=False)
        return ret


class PropellantMixCreateView(GenericCreateView):
    model = PropellantMix
    form_class = PropellantMixForm
    success_url = reverse_lazy("propellant_mix_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(PropellantMixCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("propellant_mix_detail", args=(self.object.pk,))


class PropellantMixUpdateView(UpdateView):
    model = PropellantMix
    form_class = PropellantMixForm
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(PropellantMixUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("propellant_mix_detail", args=(self.object.pk,))


class PropellantMixDeleteView(DeleteView):
    model = PropellantMix
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("propellant_mix_list")
