from django.conf.urls import url
from ..views import (EngineListView, EngineCreateView, EngineDetailView,
                     EngineUpdateView, EngineDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(EngineCreateView.as_view()),
        name="engine_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(EngineUpdateView.as_view()),
        name="engine_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(EngineDeleteView.as_view()),
        name="engine_delete"),

    url(r'^(?P<pk>\d+)/$',
        EngineDetailView.as_view(),
        name="engine_detail"),

    url(r'^$',
        EngineListView.as_view(),
        name="engine_list"),
]
