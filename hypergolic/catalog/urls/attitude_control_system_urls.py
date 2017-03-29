from django.conf.urls import url
from ..views import (AttitudeControlSystemListView, AttitudeControlSystemCreateView, AttitudeControlSystemDetailView,
                     AttitudeControlSystemUpdateView, AttitudeControlSystemDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AttitudeControlSystemCreateView.as_view()),
        name="attitude_control_system_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(AttitudeControlSystemUpdateView.as_view()),
        name="attitude_control_system_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(AttitudeControlSystemDeleteView.as_view()),
        name="attitude_control_system_delete"),

    url(r'^(?P<pk>.+)/$',
        AttitudeControlSystemDetailView.as_view(),
        name="attitude_control_system_detail"),

    url(r'^$',
        AttitudeControlSystemListView.as_view(),
        name="attitude_control_system_list"),
]
