from django.conf.urls import url
from ..views import (OrganizationListView, OrganizationCreateView, OrganizationDetailView,
                     OrganizationUpdateView, OrganizationDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(OrganizationCreateView.as_view()),
        name="organization_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(OrganizationUpdateView.as_view()),
        name="organization_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(OrganizationDeleteView.as_view()),
        name="organization_delete"),

    url(r'^(?P<pk>\d+)/$',
        OrganizationDetailView.as_view(),
        name="organization_detail"),

    url(r'^$',
        OrganizationListView.as_view(),
        name="organization_list"),
]
