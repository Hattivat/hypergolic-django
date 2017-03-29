from django.conf.urls import url
from ..views import (TankConstructionListView, TankConstructionCreateView, TankConstructionDetailView,
                     TankConstructionUpdateView, TankConstructionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(TankConstructionCreateView.as_view()),
        name="tank_construction_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(TankConstructionUpdateView.as_view()),
        name="tank_construction_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(TankConstructionDeleteView.as_view()),
        name="tank_construction_delete"),

    url(r'^(?P<pk>.+)/$',
        TankConstructionDetailView.as_view(),
        name="tank_construction_detail"),

    url(r'^$',
        TankConstructionListView.as_view(),
        name="tank_construction_list"),
]
