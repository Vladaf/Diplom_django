from django.db import models
from django.conf import settings
from django.db.models.fields import BooleanField
from django.utils import timezone
from private.models import Song

class SongLikes(models.Model):
    song_post = models.ForeignKey(
        Song,
        on_delete = models.CASCADE,
        null = True,
        verbose_name = "Song like",
    )
    liked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = "Liked by",
    )
    like = models.BooleanField(
        "Like",
        default = False,
    )
    created = models.DateTimeField(
        "Date and time",
        default = timezone.now,
    )

    def __str__(self):
        return f'{self.liked_by}: {self.song_post} {self.like}'