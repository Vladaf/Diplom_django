from django.db import models
from django.conf import settings
from django.utils import timezone
from private.models import Song

class SongComments(models.Model):
    comment = models.CharField(
        max_length = 500,
        verbose_name = "Your comment",
    )
    song_post = models.ForeignKey(
        Song,
        on_delete = models.CASCADE,
        null = True,
        verbose_name = "Song like",
    )
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = "Liked by",
    )
    created = models.DateTimeField(
        "Date and time",
        default = timezone.now,
    )

    def __str__(self):
        return f'{self.commented_by}: {self.song_post}'