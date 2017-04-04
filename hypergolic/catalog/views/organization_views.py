from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Organization
from ..forms import OrganizationForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class OrganizationListView(GenericListView):
    model = Organization
    display_data = ('description', 'illustration')


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "catalog/generic_detail.html"


class OrganizationCreateView(GenericCreateView):
    model = Organization
    form_class = OrganizationForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("organization_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(OrganizationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("organization_detail", args=(self.object.pk,))


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.modifier = self.request.user
        obj.save()
        return super(OrganizationUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("organization_detail", args=(self.object.pk,))


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("organization_list")
