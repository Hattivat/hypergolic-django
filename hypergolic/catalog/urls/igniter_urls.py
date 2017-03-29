from django.conf.urls import url
from ..views import (IgniterListView, IgniterCreateView, IgniterDetailView,
                     IgniterUpdateView, IgniterDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(IgniterCreateView.as_view()),
        name="igniter_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(IgniterUpdateView.as_view()),
        name="igniter_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(IgniterDeleteView.as_view()),
        name="igniter_delete"),

    url(r'^(?P<pk>.+)/$',
        IgniterDetailView.as_view(),
        name="igniter_detail"),

    url(r'^$',
        IgniterListView.as_view(),
        name="igniter_list"),
]
