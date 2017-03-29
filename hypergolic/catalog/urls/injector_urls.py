from django.conf.urls import url
from ..views import (InjectorListView, InjectorCreateView, InjectorDetailView,
                     InjectorUpdateView, InjectorDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(InjectorCreateView.as_view()),
        name="injector_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(InjectorUpdateView.as_view()),
        name="injector_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(InjectorDeleteView.as_view()),
        name="injector_delete"),

    url(r'^(?P<pk>\d+)/$',
        InjectorDetailView.as_view(),
        name="injector_detail"),

    url(r'^$',
        InjectorListView.as_view(),
        name="injector_list"),
]
