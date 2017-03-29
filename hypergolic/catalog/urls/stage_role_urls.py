from django.conf.urls import url
from ..views import (StageRoleListView, StageRoleCreateView, StageRoleDetailView,
                     StageRoleUpdateView, StageRoleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(StageRoleCreateView.as_view()),
        name="stage_role_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StageRoleUpdateView.as_view()),
        name="stage_role_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StageRoleDeleteView.as_view()),
        name="stage_role_delete"),

    url(r'^(?P<pk>\d+)/$',
        StageRoleDetailView.as_view(),
        name="stage_role_detail"),

    url(r'^$',
        StageRoleListView.as_view(),
        name="stage_role_list"),
]
