from django.conf.urls import url
from ..views import (NozzleTypeListView, NozzleTypeCreateView, NozzleTypeDetailView,
                     NozzleTypeUpdateView, NozzleTypeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(NozzleTypeCreateView.as_view()),
        name="nozzle_type_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(NozzleTypeUpdateView.as_view()),
        name="nozzle_type_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(NozzleTypeDeleteView.as_view()),
        name="nozzle_type_delete"),

    url(r'^(?P<pk>.+)/$',
        NozzleTypeDetailView.as_view(),
        name="nozzle_type_detail"),

    url(r'^$',
        NozzleTypeListView.as_view(),
        name="nozzle_type_list"),
]
