from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import Role
from ..forms import RoleForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class RoleListView(GenericListView):
    model = Role
    display_data = ('description', 'illustration')


class RoleDetailView(DetailView):
    model = Role
    template_name = "catalog/generic_detail.html"


class RoleCreateView(GenericCreateView):
    model = Role
    form_class = RoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("role_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RoleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("role_detail", args=(self.object.pk,))


class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RoleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("role_detail", args=(self.object.pk,))


class RoleDeleteView(DeleteView):
    model = Role
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("role_list")
