from django import forms
from typing import Dict, Any
from private.models import *


class UploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
        exclude = ["post_author", "counter"]
        widgets = {
            "band": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "band",
                    "placeholder": "Band",
                    "data-error": "Please enter Band Name",
                }
            ),
            "name": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "name",
                    "placeholder": "Name of Song",
                    "data-error": "Please enter Name of Song",
                }
            ),
            "album": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "album",
                    "placeholder": "Name of Album",
                    "data-error": "Please enter Name of Album",
                }
            ),
            "genre": forms.Select(
                attrs = {
                    "class": "form-control",
                    "id": "genre",
                    "placeholder": "Genre",
                    "data-error": "Please enter Genre",
                }
            ),
            "audio": forms.FileInput(
                attrs = {
                    "class": "form-control",
                    "id": "audio",
                    "placeholder": "Audio File",
                    "data-error": "Please upload Audio File",
                }
            ),
            "picture": forms.FileInput(
                attrs = {
                    "class": "form-control",
                    "id": "picture",
                    "placeholder": "Picture File",
                    "data-error": "Please upload Picture File",
                }
            ),
        }

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = "__all__"
        exclude = ["playlist_author"]
        widgets = {
            "name": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "name",
                    "placeholder": "name",
                    "data-error": "Please enter Playlist Name",
                }
            ),
            "picture": forms.FileInput(
                attrs = {
                    "class": "form-control",
                    "id": "picture",
                    "placeholder": "Picture File",
                    "data-error": "Please upload Picture File",
                }
            ),
        }

class SongPlaylistForm(forms.ModelForm):
    class Meta:
        model = SongPlaylist
        fields = "__all__"
        exclude = ["song"]
        widgets = {
            "playlist": forms.Select(
                attrs = {
                    "class": "form-control",
                    "id": "playlist",
                    "placeholder": "Choose playlist",
                    "data-error": "Please enter Playlist",
                }
            ),
        }