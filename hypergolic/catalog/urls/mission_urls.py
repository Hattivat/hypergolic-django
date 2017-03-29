from django.conf.urls import url
from ..views import (MissionListView, MissionCreateView, MissionDetailView,
                     MissionUpdateView, MissionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(MissionCreateView.as_view()),
        name="mission_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(MissionUpdateView.as_view()),
        name="mission_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(MissionDeleteView.as_view()),
        name="mission_delete"),

    url(r'^(?P<pk>\d+)/$',
        MissionDetailView.as_view(),
        name="mission_detail"),

    url(r'^$',
        MissionListView.as_view(),
        name="mission_list"),
]
