from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from catalog.helpers import underscore


class GenericListView(ListView):
    template_name = "catalog/generic_list.html"
    paginate_by = 20
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data(**kwargs)
        # model and display_data are provided by child view classes
        context['verbose'] = self.model._meta.verbose_name
        context['verbose_plural'] = self.model._meta.verbose_name_plural
        context['display_data'] = self.display_data
        # a hacky solution to have the link work even for still empty tables
        inspector_gadget = underscore(self.model.__name__)
        context['create_link'] = reverse('{}_create'.format(inspector_gadget))
        # if a child view class passes a filter, uses it
        try:
            filt = self.f(self.request.GET, queryset=self.model.objects.all())
            context['filter'] = filt
            context['object_list'] = filt.qs
        # otherwise tells the template not to display the associated section
        except AttributeError:
            context['filter'] = False
        return context

    def get_queryset(self):
        result = super(GenericListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            # this is needed because not all models have a 'name' field
            result = [x for x in result if query.lower() in x.__str__().lower()]
        return result


class GenericCreateView(CreateView):
    template_name = "catalog/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(GenericCreateView, self).get_context_data(**kwargs)
        context['verbose'] = self.model._meta.verbose_name
        context['verbose_plural'] = self.model._meta.verbose_name_plural
        context['model'] = self.model
        return context
