from django.urls import path
from catalog import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("discover/", views.discover, name="discover_page"),
    path("browse/", views.browse, name="browse_page"),
    path("charts/", views.charts, name="charts_page"),
    path("artists/", views.artists, name="artists_page"),
    path("", lambda request: redirect(reverse("discover_page"))),
]