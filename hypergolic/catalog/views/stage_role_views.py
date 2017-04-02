from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .base import GenericListView, GenericCreateView
from ..models import StageRole
from ..forms import StageRoleForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


class StageRoleListView(GenericListView):
    model = StageRole
    display_data = ('description', 'illustration')


class StageRoleDetailView(DetailView):
    model = StageRole
    template_name = "catalog/generic_detail.html"


class StageRoleCreateView(GenericCreateView):
    model = StageRole
    form_class = StageRoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    success_url = reverse_lazy("stage_role_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageRoleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_role_detail", args=(self.object.pk,))


class StageRoleUpdateView(UpdateView):
    model = StageRole
    form_class = StageRoleForm
    # fields = ['name', 'description', 'sources', 'illustration']
    template_name = "catalog/generic_update.html"
    initial = {}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StageRoleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("stage_role_detail", args=(self.object.pk,))


class StageRoleDeleteView(DeleteView):
    model = StageRole
    template_name = "catalog/generic_delete.html"
    success_url = reverse_lazy("stage_role_list")
