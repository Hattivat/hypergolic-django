from django.conf.urls import url
from ..views import (LifeSupportTypeListView, LifeSupportTypeCreateView, LifeSupportTypeDetailView,
                     LifeSupportTypeUpdateView, LifeSupportTypeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(LifeSupportTypeCreateView.as_view()),
        name="life_support_type_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(LifeSupportTypeUpdateView.as_view()),
        name="life_support_type_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(LifeSupportTypeDeleteView.as_view()),
        name="life_support_type_delete"),

    url(r'^(?P<pk>.+)/$',
        LifeSupportTypeDetailView.as_view(),
        name="life_support_type_detail"),

    url(r'^$',
        LifeSupportTypeListView.as_view(),
        name="life_support_type_list"),
]
