from django.conf.urls import url
from ..views import (RoleListView, RoleCreateView, RoleDetailView,
                     RoleUpdateView, RoleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RoleCreateView.as_view()),
        name="role_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RoleUpdateView.as_view()),
        name="role_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RoleDeleteView.as_view()),
        name="role_delete"),

    url(r'^(?P<pk>\d+)/$',
        RoleDetailView.as_view(),
        name="role_detail"),

    url(r'^$',
        RoleListView.as_view(),
        name="role_list"),
]
