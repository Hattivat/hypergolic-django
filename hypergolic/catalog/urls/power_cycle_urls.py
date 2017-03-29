from django.conf.urls import url
from ..views import (PowerCycleListView, PowerCycleCreateView, PowerCycleDetailView,
                     PowerCycleUpdateView, PowerCycleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PowerCycleCreateView.as_view()),
        name="power_cycle_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PowerCycleUpdateView.as_view()),
        name="power_cycle_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PowerCycleDeleteView.as_view()),
        name="power_cycle_delete"),

    url(r'^(?P<pk>\d+)/$',
        PowerCycleDetailView.as_view(),
        name="power_cycle_detail"),

    url(r'^$',
        PowerCycleListView.as_view(),
        name="power_cycle_list"),
]
