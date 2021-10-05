from django import forms
from typing import Dict, Any
from comment.models import *

class SongCommentsForm(forms.ModelForm):
    class Meta:
        model = SongComments
        fields = "__all__"
        exclude = ["song_post", "commented_by", "created"]
        widgets = {
            "comment": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "comment",
                    "placeholder": "Write comment",
                    "data-error": "Please enter Comment",
                }
            ),
        }