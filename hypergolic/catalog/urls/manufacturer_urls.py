from django.conf.urls import url
from ..views import (ManufacturerListView, ManufacturerCreateView, ManufacturerDetailView,
                     ManufacturerUpdateView, ManufacturerDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ManufacturerCreateView.as_view()),
        name="manufacturer_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(ManufacturerUpdateView.as_view()),
        name="manufacturer_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(ManufacturerDeleteView.as_view()),
        name="manufacturer_delete"),

    url(r'^(?P<pk>.+)/$',
        ManufacturerDetailView.as_view(),
        name="manufacturer_detail"),

    url(r'^$',
        ManufacturerListView.as_view(),
        name="manufacturer_list"),
]
