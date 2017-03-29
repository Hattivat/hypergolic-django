from django.conf.urls import url
from ..views import (LandingSolutionListView, LandingSolutionCreateView, LandingSolutionDetailView,
                     LandingSolutionUpdateView, LandingSolutionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(LandingSolutionCreateView.as_view()),
        name="landing_solution_create"),

    url(r'^(?P<pk>.+)/update/$',
        login_required(LandingSolutionUpdateView.as_view()),
        name="landing_solution_update"),

    url(r'^(?P<pk>.+)/delete/$',
        login_required(LandingSolutionDeleteView.as_view()),
        name="landing_solution_delete"),

    url(r'^(?P<pk>.+)/$',
        LandingSolutionDetailView.as_view(),
        name="landing_solution_detail"),

    url(r'^$',
        LandingSolutionListView.as_view(),
        name="landing_solution_list"),
]
