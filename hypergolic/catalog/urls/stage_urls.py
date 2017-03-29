from django.conf.urls import url
from ..views import (StageListView, StageCreateView, StageDetailView,
                     StageUpdateView, StageDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(StageCreateView.as_view()),
        name="stage_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StageUpdateView.as_view()),
        name="stage_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StageDeleteView.as_view()),
        name="stage_delete"),

    url(r'^(?P<pk>\d+)/$',
        StageDetailView.as_view(),
        name="stage_detail"),

    url(r'^$',
        StageListView.as_view(),
        name="stage_list"),
]
