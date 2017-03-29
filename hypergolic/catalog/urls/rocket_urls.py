from django.conf.urls import url
from ..views import (RocketListView, RocketCreateView, RocketDetailView,
                     RocketUpdateView, RocketDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RocketCreateView.as_view()),
        name="rocket_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RocketUpdateView.as_view()),
        name="rocket_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RocketDeleteView.as_view()),
        name="rocket_delete"),

    url(r'^(?P<pk>\d+)/$',
        RocketDetailView.as_view(),
        name="rocket_detail"),

    url(r'^$',
        RocketListView.as_view(),
        name="rocket_list"),
]
