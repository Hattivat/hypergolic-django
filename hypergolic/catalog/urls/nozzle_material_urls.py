from django.conf.urls import url
from ..views import (NozzleMaterialListView, NozzleMaterialCreateView, NozzleMaterialDetailView,
                     NozzleMaterialUpdateView, NozzleMaterialDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(NozzleMaterialCreateView.as_view()),
        name="nozzle_material_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(NozzleMaterialUpdateView.as_view()),
        name="nozzle_material_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(NozzleMaterialDeleteView.as_view()),
        name="nozzle_material_delete"),

    url(r'^(?P<pk>\d+)/$',
        NozzleMaterialDetailView.as_view(),
        name="nozzle_material_detail"),

    url(r'^$',
        NozzleMaterialListView.as_view(),
        name="nozzle_material_list"),
]
