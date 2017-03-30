from django.conf.urls import url
from ..views import (PropellantMixListView, PropellantMixCreateView,
                     PropellantMixDetailView, PropellantMixUpdateView,
                     PropellantMixDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PropellantMixCreateView.as_view()),
        name="propellant_mix_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PropellantMixUpdateView.as_view()),
        name="propellant_mix_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PropellantMixDeleteView.as_view()),
        name="propellant_mix_delete"),

    url(r'^(?P<pk>\d+)/$',
        PropellantMixDetailView.as_view(),
        name="propellant_mix_detail"),

    url(r'^$',
        PropellantMixListView.as_view(),
        name="propellant_mix_list"),
]
