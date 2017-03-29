from django.conf.urls import url
from ..views import (AstronautListView, AstronautCreateView, AstronautDetailView,
                     AstronautUpdateView, AstronautDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AstronautCreateView.as_view()),
        name="astronaut_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AstronautUpdateView.as_view()),
        name="astronaut_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AstronautDeleteView.as_view()),
        name="astronaut_delete"),

    url(r'^(?P<pk>\d+)/$',
        AstronautDetailView.as_view(),
        name="astronaut_detail"),

    url(r'^$',
        AstronautListView.as_view(),
        name="astronaut_list"),
]
