from django.conf.urls import url
from ..views import (TankMaterialListView, TankMaterialCreateView, TankMaterialDetailView,
                     TankMaterialUpdateView, TankMaterialDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(TankMaterialCreateView.as_view()),
        name="tank_material_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(TankMaterialUpdateView.as_view()),
        name="tank_material_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(TankMaterialDeleteView.as_view()),
        name="tank_material_delete"),

    url(r'^(?P<pk>\d+)/$',
        TankMaterialDetailView.as_view(),
        name="tank_material_detail"),

    url(r'^$',
        TankMaterialListView.as_view(),
        name="tank_material_list"),
]
