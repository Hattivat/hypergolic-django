from django.conf.urls import url
from ..views import (CompoundListView, CompoundCreateView, CompoundDetailView,
                     CompoundUpdateView, CompoundDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CompoundCreateView.as_view()),
        name="compound_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CompoundUpdateView.as_view()),
        name="compound_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CompoundDeleteView.as_view()),
        name="compound_delete"),

    url(r'^(?P<pk>\d+)/$',
        CompoundDetailView.as_view(),
        name="compound_detail"),

    url(r'^$',
        CompoundListView.as_view(),
        name="compound_list"),
]
