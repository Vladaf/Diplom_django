from django.urls import path
from private import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("", views.profile, name="profile_page"),
    path("upload/", views.upload, name="upload_page"),
    path("playlist/", views.playlist, name="playlist_page"),
    path("add_to_playlist/", views.AddToPlaylistView.as_view(), name="add_to_playlist_page"),
]