from django.conf.urls import url
from ..views import (SpacecraftListView, SpacecraftCreateView, SpacecraftDetailView,
                     SpacecraftUpdateView, SpacecraftDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SpacecraftCreateView.as_view()),
        name="spacecraft_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SpacecraftUpdateView.as_view()),
        name="spacecraft_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SpacecraftDeleteView.as_view()),
        name="spacecraft_delete"),

    url(r'^(?P<pk>\d+)/$',
        SpacecraftDetailView.as_view(),
        name="spacecraft_detail"),

    url(r'^$',
        SpacecraftListView.as_view(),
        name="spacecraft_list"),
]
