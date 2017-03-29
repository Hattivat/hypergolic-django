from django.conf.urls import url
from ..views import (HeatshieldMaterialListView, HeatshieldMaterialCreateView, HeatshieldMaterialDetailView,
                     HeatshieldMaterialUpdateView, HeatshieldMaterialDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(HeatshieldMaterialCreateView.as_view()),
        name="heatshield_material_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HeatshieldMaterialUpdateView.as_view()),
        name="heatshield_material_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HeatshieldMaterialDeleteView.as_view()),
        name="heatshield_material_delete"),

    url(r'^(?P<pk>\d+)/$',
        HeatshieldMaterialDetailView.as_view(),
        name="heatshield_material_detail"),

    url(r'^$',
        HeatshieldMaterialListView.as_view(),
        name="heatshield_material_list"),
]
