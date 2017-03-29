from django.conf.urls import url
from ..views import (CrewedMissionListView, CrewedMissionCreateView, CrewedMissionDetailView,
                     CrewedMissionUpdateView, CrewedMissionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CrewedMissionCreateView.as_view()),
        name="crewed_mission_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(CrewedMissionUpdateView.as_view()),
        name="crewed_mission_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(CrewedMissionDeleteView.as_view()),
        name="crewed_mission_delete"),

    url(r'^(?P<pk>.+)/$',
        CrewedMissionDetailView.as_view(),
        name="crewed_mission_detail"),

    url(r'^$',
        CrewedMissionListView.as_view(),
        name="crewed_mission_list"),
]
