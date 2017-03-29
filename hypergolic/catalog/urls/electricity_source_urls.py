from django.conf.urls import url
from ..views import (ElectricitySourceListView, ElectricitySourceCreateView, ElectricitySourceDetailView,
                     ElectricitySourceUpdateView, ElectricitySourceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ElectricitySourceCreateView.as_view()),
        name="electricity_source_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ElectricitySourceUpdateView.as_view()),
        name="electricity_source_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ElectricitySourceDeleteView.as_view()),
        name="electricity_source_delete"),

    url(r'^(?P<pk>\d+)/$',
        ElectricitySourceDetailView.as_view(),
        name="electricity_source_detail"),

    url(r'^$',
        ElectricitySourceListView.as_view(),
        name="electricity_source_list"),
]
