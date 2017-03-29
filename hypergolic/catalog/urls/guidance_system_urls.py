from django.conf.urls import url
from ..views import (GuidanceSystemListView, GuidanceSystemCreateView, GuidanceSystemDetailView,
                     GuidanceSystemUpdateView, GuidanceSystemDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(GuidanceSystemCreateView.as_view()),
        name="guidance_system_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(GuidanceSystemUpdateView.as_view()),
        name="guidance_system_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(GuidanceSystemDeleteView.as_view()),
        name="guidance_system_delete"),

    url(r'^(?P<pk>\d+)/$',
        GuidanceSystemDetailView.as_view(),
        name="guidance_system_detail"),

    url(r'^$',
        GuidanceSystemListView.as_view(),
        name="guidance_system_list"),
]
