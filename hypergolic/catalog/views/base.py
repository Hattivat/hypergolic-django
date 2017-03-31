from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from ..helpers import underscore


class GenericListView(ListView):
    template_name = "catalog/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data(**kwargs)
        context['verbose'] = self.model._meta.verbose_name
        context['verbose_plural'] = self.model._meta.verbose_name_plural
        context['display_data'] = self.display_data
        inspector_gadget = underscore(self.model.__name__)
        context['create_link'] = reverse('{}_create'.format(inspector_gadget))
        return context


class GenericCreateView(CreateView):
    template_name = "catalog/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(GenericCreateView, self).get_context_data(**kwargs)
        context['verbose'] = self.model._meta.verbose_name
        context['verbose_plural'] = self.model._meta.verbose_name_plural
        context['model'] = self.model
        return context
