from django.urls import path
from catalog import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("discover/", views.discover, name="discover_page"),
    path("browse/<genre_name>/", views.browse, name="browse_page"),
    path("charts/<chart_name>/", views.charts, name="charts_page"),
    path("artists/", views.artists, name="artists_page"),
    path("artists/<artist_name>/", views.artists_detail, name="artists_detail_page"),
    path("artists/<artist_name>/<album_name>/", views.albums_detail, name="albums_detail_page"),
    path("<user_name>/<playlist_name>/", views.playlist_detail, name="playlist_detail_page"),
    path("", lambda request: redirect(reverse("discover_page"))),
]