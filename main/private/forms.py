from django import forms
from typing import Dict, Any
from private.models import *


class UploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
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
            "album": forms.Select(
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