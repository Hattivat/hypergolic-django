from django.conf.urls import url
from ..views import (MissionTargetListView, MissionTargetCreateView, MissionTargetDetailView,
                     MissionTargetUpdateView, MissionTargetDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(MissionTargetCreateView.as_view()),
        name="mission_target_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(MissionTargetUpdateView.as_view()),
        name="mission_target_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(MissionTargetDeleteView.as_view()),
        name="mission_target_delete"),

    url(r'^(?P<pk>.+)/$',
        MissionTargetDetailView.as_view(),
        name="mission_target_detail"),

    url(r'^$',
        MissionTargetListView.as_view(),
        name="mission_target_list"),
]
