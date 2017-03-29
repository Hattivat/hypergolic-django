from django.conf.urls import url
from ..views import (LaunchFacilityListView, LaunchFacilityCreateView, LaunchFacilityDetailView,
                     LaunchFacilityUpdateView, LaunchFacilityDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(LaunchFacilityCreateView.as_view()),
        name="launch_facility_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(LaunchFacilityUpdateView.as_view()),
        name="launch_facility_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(LaunchFacilityDeleteView.as_view()),
        name="launch_facility_delete"),

    url(r'^(?P<pk>.+)/$',
        LaunchFacilityDetailView.as_view(),
        name="launch_facility_detail"),

    url(r'^$',
        LaunchFacilityListView.as_view(),
        name="launch_facility_list"),
]
