from django.conf.urls import url
from ..views import (RocketSeriesListView, RocketSeriesCreateView, RocketSeriesDetailView,
                     RocketSeriesUpdateView, RocketSeriesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RocketSeriesCreateView.as_view()),
        name="rocket_series_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(RocketSeriesUpdateView.as_view()),
        name="rocket_series_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(RocketSeriesDeleteView.as_view()),
        name="rocket_series_delete"),

    url(r'^(?P<pk>.+)/$',
        RocketSeriesDetailView.as_view(),
        name="rocket_series_detail"),

    url(r'^$',
        RocketSeriesListView.as_view(),
        name="rocket_series_list"),
]
