from django.conf.urls import url
from ..views import (CrewedSpacecraftListView, CrewedSpacecraftCreateView, CrewedSpacecraftDetailView,
                     CrewedSpacecraftUpdateView, CrewedSpacecraftDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CrewedSpacecraftCreateView.as_view()),
        name="crewed_spacecraft_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CrewedSpacecraftUpdateView.as_view()),
        name="crewed_spacecraft_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CrewedSpacecraftDeleteView.as_view()),
        name="crewed_spacecraft_delete"),

    url(r'^(?P<pk>\d+)/$',
        CrewedSpacecraftDetailView.as_view(),
        name="crewed_spacecraft_detail"),

    url(r'^$',
        CrewedSpacecraftListView.as_view(),
        name="crewed_spacecraft_list"),
]
