from django.conf.urls import url
from ..views import (CoolingListView, CoolingCreateView, CoolingDetailView,
                     CoolingUpdateView, CoolingDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CoolingCreateView.as_view()),
        name="cooling_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(CoolingUpdateView.as_view()),
        name="cooling_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(CoolingDeleteView.as_view()),
        name="cooling_delete"),

    url(r'^(?P<pk>.+)/$',
        CoolingDetailView.as_view(),
        name="cooling_detail"),

    url(r'^$',
        CoolingListView.as_view(),
        name="cooling_list"),
]
