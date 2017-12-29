from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^filter/artist/$', views.filter_by_artist, name="filter-artist"),
    url(r'^filter/country/$', views.filter_by_country, name="filter-country"),
]
