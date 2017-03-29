from django.conf.urls import url
from ..views import (InstrumentListView, InstrumentCreateView, InstrumentDetailView,
                     InstrumentUpdateView, InstrumentDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(InstrumentCreateView.as_view()),
        name="instrument_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(InstrumentUpdateView.as_view()),
        name="instrument_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(InstrumentDeleteView.as_view()),
        name="instrument_delete"),

    url(r'^(?P<pk>.+)/$',
        InstrumentDetailView.as_view(),
        name="instrument_detail"),

    url(r'^$',
        InstrumentListView.as_view(),
        name="instrument_list"),
]
