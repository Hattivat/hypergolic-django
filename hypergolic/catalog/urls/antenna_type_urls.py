from django.conf.urls import url
from catalog.views import (AntennaTypeListView, AntennaTypeCreateView,
                           AntennaTypeDetailView, AntennaTypeUpdateView,
                           AntennaTypeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AntennaTypeCreateView.as_view()),
        name="antenna_type_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(AntennaTypeUpdateView.as_view()),
        name="antenna_type_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(AntennaTypeDeleteView.as_view()),
        name="antenna_type_delete"),

    url(r'^(?P<pk>.+)/$',
        AntennaTypeDetailView.as_view(),
        name="antenna_type_detail"),

    url(r'^$',
        AntennaTypeListView.as_view(),
        name="antenna_type_list"),
]
