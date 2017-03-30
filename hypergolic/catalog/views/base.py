from django.views.generic.list import ListView


class BasicListView(ListView):
    template_name = "catalog/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super(BasicListView, self).get_context_data(**kwargs)
        context['verbose'] = self.model._meta.verbose_name
        context['verbose_plural'] = self.model._meta.verbose_name_plural
        context['display_data'] = self.display_data
        return context
